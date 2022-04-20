from django.db import models
from django import forms
# Create your models here.
class User(models.Model):
    name   =   models.CharField(max_length=100, null=False)
    address     =   models.CharField(max_length=250, null=False)
    username    =   models.CharField(max_length=30, null=False)
    email       =   models.EmailField(max_length=100, null=False)
    password    =   models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.name

class Book(models.Model):
    name    =   models.CharField(max_length=100, null=False)
    author  =   models.CharField(max_length=100, null=False)
    isbn    =   models.CharField(max_length=13, null=False)

    def __str__(self):
        return self.name
