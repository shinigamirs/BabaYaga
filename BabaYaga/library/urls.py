from django.urls import path

from library.rest import *

urlpatterns = [
    path('rest/book_add/', BookAddIsbn.as_view(), name='book-add-isbn'),
    path('rest/book/', BookAdd.as_view(), name='book-add-man'),
    path('rest/list/', BookList.as_view(), name='book-list'),
    path('rest/book/detail/<int:id>/', BookDetail.as_view(), name='book-detail'),
]
