#!/usr/bin/env bash

DB_NAME='gtballot' # needs to be all lower case.
DB_USERNAME='gtballot'
DB_PASSWORD='gtballot'

echo "---------------------------------------------"
echo "Running vagrant bootstrap to install requirements"
echo "---------------------------------------------"

if [ "$(whoami)" != "root" ]; then
    echo "---------------------------------------------"
    echo "This script must be run as root!"
    echo "---------------------------------------------"
    exit 1
fi

echo "---------------------------------------------"
echo "updating apt-get"
echo "---------------------------------------------"
apt-get update

echo "---------------------------------------------"
echo "installing libpq-dev python-dev used by postgresql"
echo "---------------------------------------------"
apt-get install -y libpq-dev python-dev

echo "---------------------------------------------"
echo "installing supervisor"
echo "---------------------------------------------"
apt-get install -y supervisor
cp /home/vagrant/django_shared/gtballot.conf /etc/supervisor/conf.d/gtballot.conf
mkdir -p /home/vagrant/logs/
touch /home/vagrant/logs/gunicorn_supervisor.log

echo "---------------------------------------------"
echo "installing postgresql"
echo "---------------------------------------------"
apt-get install -y postgresql postgresql-contrib

echo "---------------------------------------------"
echo "creating a database and user for postgresql"
echo "---------------------------------------------"

sudo su - postgres << START
createdb $DB_NAME
psql -c "CREATE ROLE $DB_USERNAME WITH LOGIN ENCRYPTED PASSWORD '$DB_PASSWORD';"
psql -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USERNAME;"
psql -c "ALTER USER $DB_USERNAME WITH CREATEDB"
START

echo "---------------------------------------------"
echo "installing install git"
echo "---------------------------------------------"
apt-get install -y git-core

echo "---------------------------------------------"
echo "install virtualenv"
echo "---------------------------------------------"
apt-get install -y python-virtualenv

sudo su - vagrant  << VAGRANT


echo "---------------------------------------------"
echo "create virtualenv"
echo "---------------------------------------------"
virtualenv gtballotenv
source gtballotenv/bin/activate


echo "---------------------------------------------"
echo "cloning application repository"
echo "---------------------------------------------"
git clone https://github.com/dashdrum/gtballot.git

echo "---------------------------------------------"
echo "installing django env based on a requirements file."
echo "---------------------------------------------"
pip install -r "gtballot/requirements/production.txt"

echo "---------------------------------------------"
echo "initialize database"
echo "---------------------------------------------"

export DJANGO_DEBUG=True
export DJANGO_ALLOWED_HOSTS=*
export DJANGO_SECRET_KEY='q97oy#2g_)&7qd4fanft$8aj2q(n3v6j&r646)d2r@(^bra))7'
export DJANGO_SETTINGS_MODULE=gtballot.settings.production
export DJANGO_STATIC_ROOT=/home/vagrant/gtballot/static/

cd ~/gtballot
./manage.py migrate
./manage.py loaddata ballot/fixtures/gen2014-2.json

VAGRANT

echo "---------------------------------------------"
echo "start gunicorn"
echo "---------------------------------------------"
supervisorctl reread

echo "---------------------------------------------"
echo " Finished."
echo "---------------------------------------------"

