from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from .models import Book, User
from .forms import UserRegForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

# Create your views here
class index(TemplateView):
    template_name = 'lib_man_sys/index.html'

# class UserList(ListView):
#     template_name = 'user.html'

class BookList(ListView):
    template_name = 'lib_man_sys/student.html'
    queryset = Book.objects.all()

class SignupView(CreateView):
    form_class = UserRegForm
    # success_url = reverse_lazy('login')
    template_name = 'lib_man_sys/signup.html'

# class LoginView(CreateView):