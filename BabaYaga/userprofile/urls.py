from django.conf.urls import *
from userprofile.rest import *
from userprofile.views import *

urlpatterns = [
    url(r'^rest/detail/(?P<emp_id>[\w\._-]+)/$',ProfileDetail.as_view()),
    url(r'^rest/add/(?P<emp_id>[\w\._-]+)/$',AddProfile.as_view()),
    url(r'^$', login),
    url(r'^home/$', home),
    url(r'^logout/$', logout),
]
