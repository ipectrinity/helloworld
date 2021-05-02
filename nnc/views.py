from django.shortcuts import render
from shows.models import Blog

def home_page(request):
    blogs = Blog.objects.all
    context = {'blogs' : blogs}

    return render(request, 'home.html', context)