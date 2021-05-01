from django.urls import path, include
from .views import blog, login, signup

urlpatterns = [
    path('blog/', blog, name = 'blog'),
    path('blog/login-page', login, name = 'login-page'),
    path('blog/signup-page', signup, name = 'signup-page'),
]