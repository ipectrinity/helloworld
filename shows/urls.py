from django.urls import path, include
from .views import blog_index, blog_view, login, signup, comment

urlpatterns = [
    path('blog-index/', blog_index, name = 'blog-index'),
    path('blog-index/<str:slug>', blog_view, name = "blog-view"),
    path('blog/login-page', login, name = 'login-page'),
    path('blog/signup-page', signup, name = 'signup-page'),
    path('comment',comment, name = 'comment-page'),
] 