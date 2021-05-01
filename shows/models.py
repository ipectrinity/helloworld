from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=120)
    slug        = models.SlugField()
    content     = RichTextField(blank=True, null=True)
    datetime    = models.DateTimeField(auto_now_add=True)
    image       = models.ImageField(blank=True, upload_to = 'static/')