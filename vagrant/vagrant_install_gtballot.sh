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
echo "Setup environment variables"
echo "---------------------------------------------"
sh -c "cat > /etc/profile.d/gtballot.sh" << 'EOF'
export DEBUG=True
export ALLOWED_HOSTS=*
export SECRET_KEY='q97oy#2g_)&7qd4fanft$8aj2q(n3v6j&r646)d2r@(^bra))7'
export DJANGO_SETTINGS_MODULE=gtballot.settings.production
export STATIC_ROOT=/home/vagrant/gtballot/static/
EOF

echo "---------------------------------------------"
echo "updating apt-get"
echo "---------------------------------------------"
apt-get update

echo "---------------------------------------------"
echo "installing libpq-dev python-dev used by postgresql"
echo "---------------------------------------------"
apt-get install -y libpq-dev python-dev

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
echo "installing install pip"
echo "---------------------------------------------"
apt-get install -y python-pip

echo "---------------------------------------------"
echo "cloning application repository"
echo "---------------------------------------------"

sudo su vagrant 
git clone https://github.com/dashdrum/gtballot.git

echo "---------------------------------------------"
echo "installing django env based on a requirements file."
echo "---------------------------------------------"
pip install -r "gtballot/requirements/production.txt"

echo "---------------------------------------------"
echo " Finished."
echo "---------------------------------------------"

printf "Assuming there were no errors above with postgres, here'e the info for your settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '$DB_NAME',
        'USER': '$DB_USERNAME',
        'PASSWORD': '$DB_PASSWORD',
        'HOST': 'localhost',
        'PORT': '',
    }
}
"