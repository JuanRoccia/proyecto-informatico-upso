import datetime
from flask import Blueprint, request, jsonify
from extensions import mysql
from models.data_models import Bill, Product, Service, Client
from utils.decorators import token_required, user_resource
from utils.helpers import validate_data

sales_blueprint = Blueprint('sales', __name__)

@sales_blueprint.route("/user/<int:user_id>/sales", methods=["POST"])
@token_required
@user_resource
def add_sale(user_id):
    # Set requirements and get data
    data = request.get_json()
    required = ["client_id", "products", "services"]

    # Check if all the values where sended and are not empty
    valid, error = validate_data(data, required)
    if not valid:
        return jsonify({"message": error}), 400

    # Extra validations, (check if types are correct)
    if not (isinstance(data["client_id"], int) and isinstance(data["products"], list) and isinstance(data["services"], list)):
        return jsonify({"message": "Invalid format, expected client_id:int, products:list, services:list !"}), 400
    # Extra validations, (check one of the list contains sth)
    if len(data["products"]) == 0 and len(data["services"]) == 0:
        return jsonify({"message": "Cannot accept two empty lists!"}), 400

    # Get data from POST request
    client_id = data["client_id"]
    products = data["products"]
    services = data["services"]

    # Connect to the DataBase
    cur = mysql.connection.cursor()

    # SQL Querys
    try:

        # Check if client exist
        cur.execute(f"SELECT * FROM Client WHERE idClient IN ({client_id}) AND User_idUser = {user_id}")
        data = cur.fetchone()

        # If client not found
        if not data:
            return jsonify({"message" : f"Check your client ID, client with id: {client_id} wasn't found!"})

        client = Client(data).to_json()

        # Calculate the final price
        price = 0

        # If there is more than 0 products in the list
        productList = []
        if len(products) > 0:
            # Iterate for each product
            for product_id in products:
                # Search each product
                cur.execute(f"SELECT * FROM Product WHERE idProduct IN ({product_id}) AND User_idUser = {user_id}")
                data = cur.fetchall()

                # Cancel Operation if some products are not in the DataBase
                if len(data) == 0:
                    return jsonify({"message" : f"Check your product IDs, product with id: {product_id} wasn't found!"}), 400

                # Convert Row into Object to manipulate
                product = Product(data[0])
                productList.append(product.to_json())

                # Check for stock
                if product.get_stock() <= 0:
                    return jsonify({"message" : f"Check your product IDs, product with id: {product_id} is out of stock!"}), 400

                # Add the product price to final price
                price += product.get_price()

                # Update stock
                cur.execute(f"UPDATE Product SET stock = stock - 1 WHERE idProduct = {product_id}")

        # If there is more than 0 services in the list
        serviceList = []
        if len(services) > 0:
            # Iterate for each service
            for service_id in services:
                # Search each service
                cur.execute(f"SELECT * FROM Service WHERE idService IN ({service_id}) AND User_idUser = {user_id}")
                data = cur.fetchall()

                # Cancel Operation if some services are not in the DataBase
                if len(data) == 0:
                    return jsonify({"message" : f"Check your service IDs, service with id: {service_id} wasn't found!"}), 400

                # Convert Row into Object to manipulate
                service = Service(data[0])
                serviceList.append(service.to_json())

                # Add the service price to final price
                price += service.get_price()

        # Create the bill
        date = datetime.datetime.now()
        cur.execute(f'INSERT INTO Bill (Client_idClient, price, date, User_idUser) VALUES ({client_id}, {price}, "{date}", {user_id})')

        # Get the last inserted ID
        cur.execute("SELECT LAST_INSERT_ID()")
        bill_id = cur.fetchone()
        bill_id = bill_id[0]

        # Add Products to table bill has product
        for product_id in products:
            cur.execute(f"INSERT INTO Bill_has_Product (Bill_idBill, Product_idProduct) VALUES ({bill_id}, {product_id})")

        # Add Services to table bill has service
        for service_id in services:
            cur.execute(f"INSERT INTO Bill_has_Service (Bill_idBill, Service_idService) VALUES ({bill_id}, {service_id})")

    # Catch Errors
    except Exception as Error:
        return jsonify({"message" : f"Error inserting data in the DataBase, check your values! error: {Error}"}), 400

    # Save Changes in the DB
    mysql.connection.commit()

    # Return new Bill
    return jsonify({
        "id" : bill_id,
        "client" : client,
        "price" : price,
        "date" : date,
        "products" : productList,
        "services" : serviceList,
        "user_id" : user_id
    })

@sales_blueprint.route("/user/<int:user_id>/sales/<int:bill_id>", methods=["GET"])
@token_required
@user_resource
def get_sale(user_id, bill_id):
    # Connect to the DataBase
    cur = mysql.connection.cursor()

    # SQL Query
    cur.execute(f"SELECT * FROM Bill WHERE idBill = {bill_id} AND User_idUser = {user_id}")
    data = cur.fetchone()

    # Check if Service Exist
    if not data:
        return jsonify({"message" : "Bill not found!"}), 404

    # Convert Row into Object
    objBill = Bill(data)

    # Get the client and Add client data to bill
    cur.execute(f"SELECT * FROM Client WHERE idClient = {objBill.get_client_id()} AND User_idUser = {user_id}")
    data = cur.fetchone()
    objClient = Client(data)
    objBill.set_client(objClient.to_json())

    # Search for products and add to bill
    cur.execute(f"SELECT Product.idProduct, Product.name, Product.price FROM Bill_has_Product JOIN Product ON Bill_has_Product.Product_idProduct = Product.idProduct WHERE Bill_has_Product.Bill_idBill = {bill_id}")
    data = cur.fetchall()
    objBill.set_product(data)

    # Search for products and add to bill
    cur.execute(f"SELECT Service.idService, Service.name, Service.price FROM Bill_has_Service JOIN Service ON Bill_has_Service.Service_idService = Service.idService WHERE Bill_has_Service.Bill_idBill = {bill_id}")
    data = cur.fetchall()
    objBill.set_service(data)


    # Return Bill
    return  jsonify(objBill.to_json())