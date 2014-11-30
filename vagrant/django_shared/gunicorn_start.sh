#!/bin/bash
 
NAME="gtballot" # Name of the application
DJANGODIR=/home/vagrant/gtballot # Django project directory
USER=vagrant # the user to run as
NUM_WORKERS=3 # how many worker processes should Gunicorn spawn
DJANGO_WSGI_MODULE=gtballot.wsgi # WSGI module name
 
echo "Starting $NAME as `whoami`"
 
# Activate the virtual environment
cd $DJANGODIR
source ../gtballotenv/bin/activate
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
export DJANGO_DEBUG=True
export DJANGO_ALLOWED_HOSTS=*
export DJANGO_SECRET_KEY='q97oy#2g_)&7qd4fanft$8aj2q(n3v6j&r646)d2r@(^bra))7'
export DJANGO_SETTINGS_MODULE=gtballot.settings.production
export DJANGO_STATIC_ROOT=/home/vagrant/gtballot/static/

env | sort
 
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
--name $NAME \
--workers $NUM_WORKERS \
--user=$USER \
--bind=:8000 \
--log-level=debug \
--log-file=- 

##DJANGO_SETTINGS_MODULE=gtballot.settings.production # which settings file should Django use
##export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
##GROUP=webapps # the group to run as
##SOCKFILE=/home/vagrant/gtballot/run/gunicorn.sock # we will communicte using this unix socket
 
# Create the run directory if it doesn't exist
##RUNDIR=$(dirname $SOCKFILE)
##test -d $RUNDIR || mkdir -p $RUNDIR

## --group=$GROUP \
## --bind=unix:$SOCKFILE \