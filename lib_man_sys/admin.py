from django.contrib import admin
from .models import Book, User
# Register your models here.

mymodels = [User, Book]
admin.site.register(mymodels)
