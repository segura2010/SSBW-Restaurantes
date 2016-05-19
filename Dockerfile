from debian:jessie
maintainer yo@correo.es

# variables de ambiente
#     código (solo lectura)
env project_dir /restaurantes
#     datos: MEDIA_ROOT, db.sqlite (lectura y escritura)
env volume_dir /var/Volumes/restaurantes

run apt-get -y update

# lo mínimo para django
run apt-get install -y apt-utils
run apt-get install -y python python-dev python-setuptools

# Instala mongo
# Import MongoDB public GPG key AND create a MongoDB list file
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
RUN echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.0.list

RUN apt-get install -y mongodb-org --force-yes

RUN apt-get install -y mongodb-org=3.0.1 mongodb-org-server=3.0.1 mongodb-org-shell=3.0.1 mongodb-org-mongos=3.0.1 mongodb-org-tools=3.0.1 --force-yes



# para instalar pip
run apt-get install -y git                                                                                             
run easy_install -U pip    

# donde va a estar la aplicación
add . ${project_dir}
workdir $project_dir

run pip install -r requeriments.txt


# PRODUCCION
run pip install gunicorn

# servidor web y watchdog
run apt-get install -y supervisor nginx

#  configuraciones
run cp  despliegue/supervisor.conf /etc/supervisor/conf.d/
run cp  despliegue/nginx-default /etc/nginx/sites-available/default

run sed -i 's/DEBUG = True/DEBUG= False/' Restaurantes/settings.py

expose 80

cmd despliegue/collect_static.sh && supervisord
