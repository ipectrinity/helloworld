from django.db import models

# Create your models here.
class ContactForm(models.Model):
    name   = models.CharField(max_length=45)
    email    = models.EmailField(max_length=50)
    message  = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return (self.name + ' - ' + self.email)