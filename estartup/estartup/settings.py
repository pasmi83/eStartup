"""
Django settings for estartup project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import posixpath
import psycopg2
from django.contrib.messages import constants as messages
from  estartup.secret_key import EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT, EMAIL_USE_TLS
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1k+eox2sy@+=k0^n3+79d#*&d*c%du(mxd420vx(fyj7c8c%^h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_cleanup',
    'taggit',
    'easy_thumbnails',
    'widget_tweaks',
    'phonenumber_field',

    'pages',
    'tutors',
    'courses',
    'projects',
    'feedbacks',
    'announcements',
    'leads',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'estartup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')], #ссылка на папку шаблонов
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

WSGI_APPLICATION = 'estartup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {"default": {
        "ENGINE":"django.db.backends.postgresql",
        "NAME":"estartup",
        "USER":"postgres",
        "PASSWORD":"3891144",
        "HOST":"localhost",
        "PORT":"5433",
        }}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATE_INPUT_FORMATS=(
    '%d.%m.%Y', '%Y-%m-%d', '%d.%m.%y',# '25.10.2006', '25.10.2006', '25.10.06'
    '%d-%m-%Y', '%d/%m/%Y', '%d/%m/%y',# '25-10-2006', '25/10/2006', '25/10/06'
    '%d %b %Y',# '25 Oct 2006', 
    '%d %B %Y',# '25 October 2006', 
)
DATETIME_INPUT_FORMATS=(
    '%d.%m.%y %H:%M', '%d.%m.%y %H:%M:%S','%d.%m.%Y %H:%M', '%d.%m.%Y %H:%M:%S','%Y-%m-%d %H:%M:%S',
   '%Y-%m-%d %H:%M:%S.%f', '%Y-%m-%d%H:%M',
  '%Y-%m-%d', '%m/%d/%Y %H:%M:%S', '%m/%d/%Y %H:%M:%S.%f',
  '%m/%d/%Y %H:%M', '%m/%d/%Y', '%m/%d/%y %H:%M:%S',
 '%m/%d/%y %H:%M:%S.%f', 
 '%m/%d/%y %H:%M', '%m/%d/%y')
DATE_FORMAT = 'd.m.Y'
DATETIME_FORMAT = 'd.m.Y HH:MM:SS'



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'estartup/static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')


TAGGIT_CASE_INSENSITIVE = True

PHONENUMBER_DEFAULT_REGION = 'RU'

MESSAGE_TAGS = {
messages.INFO: 'success',
messages.ERROR: 'danger'
}