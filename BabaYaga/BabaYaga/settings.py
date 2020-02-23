"""
Django settings for BabaYaga project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p8^84!$^td5@uaer8!xc7opb%-a(i0ylwf*_q-!6ph+wb$gm__'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['babayaga.esec.coriolis.in', '172.20.4.115', '127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'library',
    'drf_yasg',
    'book_issue',
    'userprofile',
]

SWAGGER_SETTINGS = {
    'JSON_EDITOR': True,
    'SECURITY_DEFINITIONS': {
        'api_Key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        },
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'BabaYaga.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'BabaYaga.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend"
]

import ldap
from django_auth_ldap.config import LDAPSearch
from .ldap_config import *
ldap_file_name = 'BabaYaga/ldap.json'
md5_file_name = 'BabaYaga/md5.txt'

if os.path.exists(ldap_file_name):
    import json
    try:
        with open(ldap_file_name) as ldap_json:
            data = json.load(ldap_json)

        original_md5 = open(md5_file_name).read()
        returned_md5 = md5_generator(ldap_file_name)

        if original_md5 == returned_md5 and check_ldap_connection(data):
            AUTHENTICATION_BACKENDS.append("django_auth_ldap.backend.LDAPBackend")
            AUTH_LDAP_SERVER_URI = data.get("ldap_server_uri")
            AUTH_LDAP_BIND_DN = data.get("ldap_bind_dn")
            AUTH_LDAP_BIND_PASSWORD = data.get("ldap_bind_password")
            ldap_search = data.get("ldap_search")
            AUTH_LDAP_USER_SEARCH = LDAPSearch(
                ldap_search , ldap.SCOPE_SUBTREE, "(uid=%(user)s)"
            )
    except Exception:
        pass

