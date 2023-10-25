import os
from flask_mysqldb import MySQL
from decouple import config

class Config:
    # Directorios de plantillas y archivos estáticos
    TEMPLATE_DIR = os.path.abspath('./frontend')
    STATIC_DIR = os.path.abspath('./frontend/static')

    # Configuración de Flask
    TEMPLATE_FOLDER = TEMPLATE_DIR
    STATIC_FOLDER = STATIC_DIR

    # Configuración de MySQL
    MYSQL_HOST = config('MYSQL_HOST')
    MYSQL_USER = config('MYSQL_USER')
    MYSQL_PASSWORD = config('MYSQL_PASSWORD')
    MYSQL_DB = config('MYSQL_DB')

    # Clave secreta
    SECRET_KEY = config('SECRET_KEY')
