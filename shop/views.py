from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Orders, OrderUpdate
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt 

# Create your views here.

def index(request):    
    allProds = []
    #Getting all names of categories
    catProds = Product.objects.values('category', 'product_id')
    #Getting unique names of categories
    cats = {item['category']  for item in catProds}
    
    for cat in cats:
        #Filtering products based on category
        prods = Product.objects.filter(category=cat)
        n = len(prods)
        nSlides = n//4 + ceil((n/4) - (n//4))
        allProds.append([prods, range(1, nSlides), nSlides])
    
    params = {
        'allProds' : allProds
    }
    return render(request, 'shop/index.html', params)

def searchMatch(query, item):
    ''' Return True only if search matches'''
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower() or query in item.subcategory.lower(): 
        return True 
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catProds = Product.objects.values('category', 'product_id')
    cats = {item['category']  for item in catProds}
     
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prods = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prods)
        nSlides = n//4 + ceil((n/4) - (n//4))
        if n != 0:
            allProds.append([prods, range(1, nSlides), nSlides])
    
    params = {
        'allProds' : allProds,
        'msg' : ''
    }
    
    if len(allProds) == 0 or len(query) < 4:
        params = {'msg' : 'Please make sure to enter relevent search query'}
        
    return render(request, 'shop/search.html', params)

    

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    thank = False
    if request.method == 'POST': 
        name = request.POST.get('username', '')
        email = request.POST.get('useremail', '')
        phone = request.POST.get('number', '')
        query = request.POST.get('query', '')
        
        contact = Contact(name=name, email=email, phone=phone, desc=query)
        contact.save()
        thank = True 
    return render(request, 'shop/contact.html', {'thank' : thank})


def productView(request, myid):
    product = Product.objects.filter(product_id = myid)
    
    return render(request, 'shop/productView.html', {'product' : product[0]})

def cart(request):
    products = Product.objects.all()
    params = {'products' : products,}
    return render(request, 'shop/cart.html', params)

def tracker(request):
    if request.method == 'POST': 
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')

        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                
                response = json.dumps({'status' : 'success', 'updates' : updates, 'itemsJson' : order[0].items_json}, default=str)
                # response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response, content_type='application/json')
                # return HttpResponse(response, order)
            else:
                return HttpResponse({'status' : 'no items'})
                # return HttpResponse('No such order found.', content_type='text/plain')
        
        except Exception as e:
            return HttpResponse({'status' : 'error'})
            # return HttpResponse(f'Error: {str(e)}', content_type='text/plain')
    
    return render(request, 'shop/tracker.html')

def checkout(request):
    if request.method == 'POST': 
        items_json = request.POST.get('itemsJson','')
        amount = request.POST.get('amount', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zipcode', '')
        
        #updating order along with order update
        order = Orders(items_json=items_json, amount=amount, name=name, email=email, phone=phone, address=address1, address_2 = address2, state=state, city=city, zip_code=zip_code)
        order.save()
        #updating order here
        update = OrderUpdate(order_id=order.order_id, update_desc='The order has been placed')
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id':id})
        # Request paytm to transfer the amount to merchent account
    return render(request, 'shop/checkout.html')


@csrf_exempt
def handlerequest(request):
    #paytm will send you payment request 
    pass