from django.urls import path
from .views import index, UserList, BookList
urlpatterns = [
    path('', index.as_view(), name='index'),
    path('student/', BookList.as_view(), name='student'),
    path('user/', UserList.as_view(), name='user'),
]