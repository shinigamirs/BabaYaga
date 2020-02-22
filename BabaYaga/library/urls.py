from django.conf.urls import *

from library.rest import *

urlpatterns = [
    url(r'^rest/book_add/$', BookAddIsbn.as_view()),
    url(r'^rest/book/$', BookAdd.as_view()),
    url(r'^rest/list/$', BookList.as_view()),
    url(r'^rest/add-group/(?P<id>[\d]+)/$', BookDetail.as_view()),
]
