from django.urls import path, include
from .views import contact
from django.contrib import admin

##ADMIN SITE CONFIGURATIONS##
admin.site.site_header = "Netflix'n'Chill"
admin.site_title = "Welcome to the DashBoard"
admin.site.index_title = "Welcome to admin's Den"


urlpatterns = [
    path('contact-us/', contact, name = "contact-us")
]

