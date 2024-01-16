# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Category, NewsContent

# Register your models here.


admin.site.register(NewsContent)
admin.site.register(Category)
