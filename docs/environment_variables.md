# GTBallot Environment Variables

DJANGO_ALLOWED_HOSTS='dangentry.com','example.com'
DJANGO_ALLOWED_HOSTS='\*' *# Allows any host*

DJANGO_DEBUG=True *# Only include this variable to set DEBUG to True. Omit to default to False*

DJANGO_SETTINGS_MODULE=gtballot.settings.development 

DJANGO_SECRET_KEY=‘*some secret string*’ *# Use a different key for each instance (DEV, PROD, etc)*

DJANGO_STATIC_ROOT=“/home/user/app/static/“ *# Only needed when DEBUG is False*
