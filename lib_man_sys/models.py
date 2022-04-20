from django.db import models

# Create your models here.
class AdminUser(models.Model):
    name   =   models.CharField(max_length=100, null=False)
    address     =   models.CharField(max_length=250, null=False)
    username    =   models.CharField(max_length=30, null=False)
    email       =   models.EmailField(max_length=100, null=False)
    password    =   models.CharField(max_length=20, null=False)


class Books(models.Model):
    name    =   models.CharField(max_length=100, null=False)
    author  =   models.CharField(max_length=100, null=False)
    isbn    =   models.CharField(max_length=13, null=False)

