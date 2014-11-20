#  Development settings

from .base import *


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

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': join(BASE_DIR, 'db.sqlite3'),
#     }
# }

## Django Debug Toolbar settings

INSTALLED_APPS += ('debug_toolbar',)
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    
## end Django Debug Toolbar settings