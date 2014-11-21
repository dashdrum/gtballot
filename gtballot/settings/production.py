# Production settings

from .base import *

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gtballot',
        'USER': 'gtballot',
        'PASSWORD': 'gtballot',
        'HOST': 'localhost',
        'PORT': '',
    }
}
