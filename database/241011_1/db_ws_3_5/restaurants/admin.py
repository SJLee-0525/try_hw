from django.contrib import admin
from .models import Category, Restaurant, Menu

# Register your models here.
admin.site.register(Category)
admin.site.register(Restaurant)
admin.site.register(Menu)
