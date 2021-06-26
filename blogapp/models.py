from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = RichTextField()