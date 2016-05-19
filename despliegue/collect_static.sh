#/bin/bash
cp -r static/ /var/www/static
#cp -r media/ /var/www/media

# Inicia MongoDB
/usr/bin/mongod &

# Inicia gunicorn
/usr/local/bin/gunicorn Restaurantes.wsgi:application --bind 0.0.0.0:8000
