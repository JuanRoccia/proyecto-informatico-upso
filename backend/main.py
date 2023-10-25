from flask import Flask
from flask_mysqldb import MySQL
from config.settings import Config
from views.users import users_blueprint
from views.stock import stock_blueprint
from views.services import services_blueprint
from views.sales import sales_blueprint
from views.clients import clients_blueprint
from utils.helpers import encode_password
from utils.decorators import token_required, user_resource
from extensions import app, mysql

# Registro de las rutas
app.register_blueprint(users_blueprint)
app.register_blueprint(stock_blueprint)
app.register_blueprint(services_blueprint)
app.register_blueprint(sales_blueprint)
app.register_blueprint(clients_blueprint)

if __name__ == "__main__":
    app.run()
