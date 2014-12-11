"""
Django settings for gtballot project.
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from os.path import join, abspath, dirname
from os import environ

BASE_DIR = join(abspath(dirname(__file__)), '..','..')


#SECRET_KEY = '3i1a^9&k!8i1+am1g1@v##=&1v*%=$24#pgxdfi-ms3dkg$^03'
SECRET_KEY = environ['DJANGO_SECRET_KEY']

DEBUG = bool(environ.get('DJANGO_DEBUG', False))

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = environ['DJANGO_ALLOWED_HOSTS'].split(',')


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',

    'ballot',
)

## Django 1.7 middleware

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

import django

if django.get_version() < '1.7':

    ## Django 1.6 middleware

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

if django.get_version() < '1.6':

    ## Django 1.5 middleware (works for 1.4 also)
    
    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    )

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    join(BASE_DIR, 'gtballot/templates').replace ('\\','/'),
)

ROOT_URLCONF = 'gtballot.urls'

WSGI_APPLICATION = 'gtballot.wsgi.application'

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    join(BASE_DIR, "gtballot/static"),
)

STATIC_ROOT = environ['DJANGO_STATIC_ROOT']

# Other

CRISPY_TEMPLATE_PACK = 'bootstrap3'

