# Imagen base usada python
FROM python:latest

# Instalar librerias de python para trabajar con memcached
RUN pip3 install pymemcache
RUN pip3 install mysql-connector-python

# Creamos el directorio de trabajo
WORKDIR /usr/src/app

# Añadimos el script al contenedor
COPY memcached.py ./
