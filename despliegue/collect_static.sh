#/bin/bash
cp -r static/ /var/www/static
#ln -r media/ /var/www/media


# Inicia MongoDB
/usr/bin/mongod &

# Inicia nginx
service nginx start

# Pobla BD
/usr/bin/python populate.py

# Inicia gunicorn
/usr/local/bin/gunicorn Restaurantes.wsgi:application --bind 0.0.0.0:8000
