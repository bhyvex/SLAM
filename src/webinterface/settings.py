import sys
import os

"""
Django settings for slam project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'Must_be_modified'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Hosts allowed to access the application (prevent HTTP header attacks)
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'slam',
    'webinterface'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    # TODO: Active csrf
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'webinterface.middleware.HttpMethodsMiddleware',
    'webinterface.middleware.LoginRecordMiddleware'
)

ROOT_URLCONF = 'webinterface.urls'

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

WSGI_APPLICATION = 'webinterface.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING = {'version': 1,
           'disable_existing_loggers': False,
           'handlers': {
               'file': {
                   'level': 'DEBUG',
                   'class': 'logging.StreamHandler',
               }
           },
           'loggers': {
               'django.request': {
                   'handlers': ['file'],
                   'level': 'DEBUG',
                   'propagate': True,
                   },
               }
           }

# Login redirection
LOGIN_URL = '/login'


# Site configuration overrides defaults defined here.
# Look for site configuration first in the conf/ directory at the same level
# as the src/ directory, then, if not found, in /etc/slam.
root_dir = os.path.abspath(__file__)
# CONF_PARENT_DIR_LEVEL_UP is the number of directory level to go up
# from current module directory to find conf/ parent
CONF_PARENT_DIR_LEVEL_UP = 2
for i in range(CONF_PARENT_DIR_LEVEL_UP+1):
    root_dir = os.path.dirname(root_dir)
sys.path.insert(0, "/etc/slam")
sys.path.insert(0, os.path.join(root_dir,'conf'))
from configuration import *

