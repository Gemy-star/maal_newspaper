from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True)


# Create your models here.
class NewsContent(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    body = RichTextField()
    news_photo = models.ImageField(null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
