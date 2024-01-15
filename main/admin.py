from django.contrib import admin
from .models import NewsContent
from .models import Category

# Register your models here.


admin.site.register(NewsContent)
admin.site.register(Category)
