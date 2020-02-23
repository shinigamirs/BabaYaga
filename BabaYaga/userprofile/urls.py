from django.conf.urls import *
from userprofile.rest import *


urlpatterns = [
    url(r'^rest/profile/(?P<emp_id>[\w\._-]+)/$',ProfileDetail.as_view()),
    url(r'^rest/add/(?P<emp_id>[\w\._-]+)/$',AddProfile.as_view()),
]
