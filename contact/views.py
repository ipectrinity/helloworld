from django.shortcuts import render
from .models import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def contact(request):

    context = {}

    if request.method == 'POST':
        name    = request.POST['name']
        email   = request.POST['email']
        message = request.POST['message']

        contacts = ContactForm(name=name, email=email, message=message)
        contacts.save()

        ############
        subject = 'NoReply: Netflix and Chill'
        reply =  """
Hey there! 
Thanks for contacting us! We appreciate your messages, and we've watched your message!
Stay tuned to be the Netflix Junkie! 😉😎 
~ Admin Of Netflix-and-Chill"""
        ############


        #sending mail
        send_mail(
            subject,#subject
            reply,#message
            settings.EMAIL_HOST_USER,#from mail
            [email],#to mail >> a list of mailss
            fail_silently=False,
        )

    return render(request, 'contact.html', context)