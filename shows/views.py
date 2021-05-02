from django.shortcuts import render
from .models import Blog

# Create your views here.
def blog_index(request):
    #loading the dataset as whole
    blog = Blog.objects.all
        #blog-model data

    context = {
        'blog' : blog
    }


    return render(request, 'blog-index.html', context)



def blog_view(request):
    blog = Blog.objects.all

    context = {
        'blog' : blog
    }

    return render(request, 'blog-view.html', context)



def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def comment(request):
    return render(request, 'comment.html')