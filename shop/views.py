from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
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
    catProds = Product.objects.values('category', 'id')
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
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request):
    return HttpResponse("We are at productview")

def checkout(request):
    return HttpResponse("We are at checkout")
