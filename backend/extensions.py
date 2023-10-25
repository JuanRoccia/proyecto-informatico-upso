from flask import Flask
from flask_mysqldb import MySQL
from flask_cors import CORS
from config.settings import Config
import os

template_dir = os.path.abspath('./frontend')
static_dir = os.path.abspath('./frontend/static')

app = Flask(__name__, template_folder=Config.TEMPLATE_DIR, static_folder=Config.STATIC_DIR)
app.config.from_object(Config)
mysql = MySQL(app)
CORS(app)