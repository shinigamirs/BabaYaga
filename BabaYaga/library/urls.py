from django.urls import path

from library.rest import *
from library.views import *

urlpatterns = [
    path('rest/book_add/', BookAddIsbn.as_view()),
    path('rest/book/', BookAdd.as_view()),
    path('rest/list/', BookList.as_view()),
    path('rest/book/detail/<int:id>/', BookDetail.as_view()),
    path('book/list/', book_list, name='book-list'),
]
