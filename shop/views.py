from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Orders
from math import ceil

# Create your views here.

def index(request):
    # products = Product.objects.all()
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    
    # params = {
    #     'no_of_slides' : nSlides,
    #     'product' : products,
    #     'range' : range(1, nSlides)
    # }
    
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    
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

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method == 'POST': 
        name = request.POST.get('username', '')
        email = request.POST.get('useremail', '')
        phone = request.POST.get('number', '')
        query = request.POST.get('query', '')
        
        contact = Contact(name=name, email=email, phone=phone, desc=query)
        contact.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request, myid):
    product = Product.objects.filter(product_id = myid)
    
    return render(request, 'shop/productView.html', {'product' : product[0]})

def cart(request):
    products = Product.objects.all()
    params = {'products' : products,}
    return render(request, 'shop/cart.html', params)

def checkout(request):
    if request.method == 'POST': 
        items_json = request.POST.get('itemsJson','')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zipcode', '')
        
        order = Orders(items_json=items_json, name=name, email=email, phone=phone, address=address1, address_2 = address2, state=state, city=city, zip_code=zip_code)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id':id})
    
    products = Product.objects.all()
    params = {'products' : products,}
    return render(request, 'shop/checkout.html', params)
