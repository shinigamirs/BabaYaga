from django.conf.urls import *
from book_issue.rest import *


urlpatterns = [
    url(r'^rest/issue/$',IssueBook.as_view()),
    url(r'^rest/return/$',ReturnBook.as_view()),
]
