from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from .models import Book, User
# Create your views here
class index(TemplateView):
    template_name = 'lib_man_sys/index.html'

class UserList(ListView):
    template_name = 'user.html'

class BookList(ListView):
    template_name = 'lib_man_sys/student.html'
    queryset = Book.objects.all()
