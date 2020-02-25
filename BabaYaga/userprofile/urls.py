from django.conf.urls import *
from userprofile.rest import *
from userprofile.views import *

urlpatterns = [
    url(r'^rest/detail/(?P<emp_id>[\w\._-]+)/$',ProfileDetail.as_view()),
    # url(r'^rest/add/(?P<emp_id>[\w\._-]+)/$',AddProfile.as_view()),
    url(r'^$', login, name='login'),
    url(r'^home/$', home, name='home'),
    url(r'^logout/$', logout, name='logout'),
]
