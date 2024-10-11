from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

def blogpost(request, id):
    #We are cathing id which is send from urlpatterns
    # we [0] because to get 'About Myself' from <QuerySet [<Blogpost: About Myself>]>
    # Then filtered post will be catched in blogpost.html
    post = Blogpost.objects.filter(post_id = id)[0]
    return render(request, 'blog/blogpost.html', {'post' : post})