from django.urls import path
from .views import index, SignupView, BookList
urlpatterns = [
    path('', index.as_view(), name='index'),
    path('student/', BookList.as_view(), name='student'),
    path('signup/', SignupView.as_view(), name='signup'),
    # path('login/', LoginView.as_view(), name='login'),
 ]