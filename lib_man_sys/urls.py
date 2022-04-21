from django.urls import path
from .views import index, SignupView, BookList
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('', index.as_view(), name='home'),
    path('student/', BookList.as_view(), name='student'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='lib_man_sys/login.html'), name='login'),
 ]