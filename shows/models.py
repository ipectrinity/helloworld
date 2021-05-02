from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=120)
    slug        = models.SlugField()
    content     = RichTextField(blank=True, null=True)
    datetime    = models.DateTimeField(auto_now_add=True)
    link        = models.CharField(blank=True, max_length=150)
    image       = models.ImageField(blank=True, upload_to = 'static/')

    def __str__(self):
        return self.title + ' | ' + str(self.datetime.date())