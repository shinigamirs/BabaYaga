"""BabaYaga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import include, url, static

from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
admin.autodiscover()

urlpatterns = [

    path('admin/', admin.site.urls),
    path('library/', include('library.urls')),
    url(r'^library/', include('library.urls')),
    url(r'^book_issue/', include('book_issue.urls')),
    url(r'', include('userprofile.urls')),
    path('social', include('social_django.urls', namespace='social')),

]

schema_view = get_schema_view(
    openapi.Info(
        title="BabaYaga API",
        default_version='v1',
        description="BabaYaga REST API Documentation",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns.append(path('api_doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'))
