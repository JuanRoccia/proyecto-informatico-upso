import hashlib,base64,jwt,os, datetime
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from models import Client, Product, Service, Bill
from flask import render_template
from functools import wraps
from flask_cors import CORS

# * CONFIG -------------------------------------------------------------------------
template_dir = os.path.abspath('./frontend')
static_dir = os.path.abspath('./frontend/static')
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
CORS(app)

app.config['MYSQL_HOST'] = 'mysql-ivangonzaloooo.alwaysdata.net'
app.config['MYSQL_USER'] = '330942'
app.config['MYSQL_PASSWORD'] ='Proyecto-1'
app.config['MYSQL_DB'] = 'ivangonzaloooo_proyecto'
app.config['SECRET_KEY'] = 'wFJL3nKbZ8xhvXAdG92cYsVqMp7mOtU0QeTBo1Hl4g5i6IuNykSrfDzaRCXPW'

mysql = MySQL(app)

# * VIEWS --------------------------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")


# * USERS --------------------------------------------------------------------------
def encode_password(password, seed):
    b_seed = seed.encode('utf-8')
    b_password = password.encode('utf-8')
    encoded_password = hashlib.pbkdf2_hmac('sha256', b_password, b_seed, 100000)
    encoded_password_b64 = base64.b64encode(encoded_password).decode('utf-8')
    return encoded_password_b64

@app.route('/user/register', methods = ["POST"])
def register_user():
    # Set requirements and get data
    data = request.get_json()
    required = ["name", "username", "password", "email"]

    # Check if all the values where sended and are not empty
    for field in required:

        # Check if field exist
        if field not in data:
            return jsonify({"message" : f"Missing '{field}' in the JSON"}), 400
        # Check if field is not empty

        if data[field] == "":
            return jsonify({"message" : f"The attribute '{field}' cannot be empty"}), 400

    # Get data from POST request
    name = data["name"]
    username = data["username"]
    password = data["password"]
    email = data["email"]

    # Connect to the DataBase
    cur = mysql.connection.cursor()

    # SQL Query
    cur.execute(f'SELECT * FROM User WHERE email = "{email}"')
    data = cur.fetchall()

    # Check if email already exist
    if data:
        return jsonify({"message" : "Already registered email!"}), 409

    # Encode Password
    encoded_password = encode_password(password, app.config["SECRET_KEY"])

    # SQL Query
    cur.execute(f'INSERT INTO User (name, username, password, email) VALUES ("{name}","{username}", "{encoded_password}", "{email}")')

    # Save Changes in the DB
    mysql.connection.commit()

    # Get the last inserted ID
    cur.execute("SELECT LAST_INSERT_ID()")
    new_id = cur.fetchone()
    new_id = new_id[0]

    # Return the added user
    return jsonify({
        "id" : new_id,
        "name" : name,
        "username" : username,
        "email" : email
        })

@app.route('/user/login', methods=['POST'])
def login():
    # Extract data from Log In
    auth = request.authorization

    # Check if data is provided
    if not auth or not auth.username or not auth.password:
        return jsonify({"message" : "Not autorized!"}), 401

    # Encode Password
    password = encode_password(auth.password, app.config["SECRET_KEY"])

    # Connect to the DataBase
    cur = mysql.connection.cursor()

    # SQL Query
    cur.execute(f'SELECT * FROM User WHERE email = "{auth.username}" AND password = "{password}"')
    row = cur.fetchone()

    # Check if data is correct
    if not row:
        return jsonify({"message" : "Not autorized!"}), 401

    # User Exist and match in the DB
    token = jwt.encode({
        "id" : row[0],
        "exp" : datetime.datetime.utcnow() + datetime.timedelta(minutes = 100)
    }, app.config["SECRET_KEY"])


    return jsonify({"token" : token, "username" : row[2], "id" : row[0]})


# * DECORATORS ---------------------------------------------------------------------
def token_required(func):
    @wraps(func)
    def token_wrapper(*args, **kwargs):
        # Check if token header exist
        token = None
        if "token" in request.headers:
            token = request.headers["token"]

        # Return error if not recived
        if not token:
            return jsonify({"message" : "Token missing!"}), 401

        # Check if useser id header exist
        user_id = None
        if "user-id" in request.headers:
            user_id = request.headers["user-id"]

        # Return error if not recived
        if not user_id:
            return jsonify({"message" : "User missing!"}), 401

        # Decode Token
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms = ["HS256"])
            token_id = data["id"]

            # Return error if user does not match
            if int(user_id) != int(token_id):
                return jsonify({"message" : "ID provided does not match!"}), 401

        # Catch any errors and return them
        except Exception as error:
            return jsonify({"message" : str(error)}), 401

        # Resume execution
        return func(*args, **kwargs)
    return token_wrapper

def user_resource(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        # Extract id from header and route
        id_user_route = kwargs["user_id"]
        user_id = request.headers["user-id"]

        # Check if id match
        if int(id_user_route) != int(user_id):
                return jsonify({"message": "You do not have permission to access this resource!"}), 403

        # Resume execution
        return func(*args, **kwargs)
    return decorated


# * STOCK --------------------------------------------------------------------------
@app.route("/user/<int:user_id>/products", methods = ["GET"])
@token_required
@user_resource
def get_products_list(user_id):
    # Connect to the DataBase
    cur = mysql.connection.cursor()

    # SQL Query
    cur.execute("SELECT * FROM Product WHERE User_idUser = {0}".format(user_id))
    data = cur.fetchall()

    # Convert Rows
    productsList = []
    for row in data:
        objProduct = Product(row)
        productsList.append(objProduct.to_json())

    # Return List
    return  jsonify(productsList)

@app.route("/user/<int:user_id>/products", methods = ["POST"])
@token_required
@user_resource
def add_products(user_id):
    # Set requirements and get data
    data = request.get_json()
    required = ["name", "description", "price", "stock"]

    # Check if all the values where sended and are not empty
    for field in required:

        # Check if field exist
        if field not in data:
            return jsonify({"message" : f"Missing '{field}' in the JSON"}), 400

        # Check if field is not empty
        if isinstance(data[field], str) and data[field] == "":
            return jsonify({"message" : f"The attribute '{field}' cannot be empty"}), 400
        if (isinstance(data[field], int) or isinstance(data[field], float)) and data[field] < 0:
            return jsonify({"message" : f"The attribute '{field}' cannot be lower than 0"}), 400

    # Get data from POST request
    name = data["name"]
    description = data["description"]
    price = data["price"]
    stock = data["stock"]

    # Connect to the DataBase
    cur = mysql.connection.cursor()

    # SQL Query
    try:
        cur.execute(f'INSERT INTO Product (name, description, price, stock, User_idUser) VALUES ("{name}","{description}", {price}, {stock}, {user_id})')

    # Catch Errors
    except:
        return jsonify({"message" : "Error inserting data in the DataBase, check your values!"}), 400

    # Save Changes in the DB
    mysql.connection.commit()

    # Get the last inserted ID
    cur.execute("SELECT LAST_INSERT_ID()")
    new_id = cur.fetchone()
    new_id = new_id[0]

    # Return the added product
    return jsonify({
        "id" : new_id,
        "name" : name,
        "description" : description,
        "price" : price,
        "stock" : stock,
        "user_id" : user_id
        })

@app.route("/user/<int:user_id>/products/<int:product_id>", methods = ["GET"])
@token_required
@user_resource
def get_product(user_id, product_id):
    # Connect to the DataBase
    cur = mysql.connection.cursor()

    # SQL Query
    cur.execute(f"SELECT * FROM Product WHERE idProduct = {product_id} AND User_idUser = {user_id}")
    data = cur.fetchone()

    # Check if Product Exist
    if not data:
        return jsonify({"message" : "Product not found!"}), 404

    # Convert Row into Object
    objProduct = Product(data)

    # Return Product
    return  jsonify(objProduct.to_json())

@app.route("/user/<int:user_id>/products/<int:product_id>", methods = ["DELETE"])
@token_required
@user_resource
def delete_product(user_id, product_id):
    # Connect to the DataBase
    cur = mysql.connection.cursor()

    # SQL Query
    cur.execute(f"DELETE FROM Product WHERE idProduct = {product_id} AND User_idUser = {user_id}")

    # Save Changes in the DB
    mysql.connection.commit()

    # Return Confirmation Message
    return jsonify({"message" : "Deleted", "id" : product_id})

@app.route("/user/<int:user_id>/products/<int:product_id>", methods = ["PUT"])
@token_required
@user_resource
def modify_product(user_id, product_id):
    # Set requirements and get data
    data = request.get_json()
    required = ["name", "description", "price", "stock"]

    # Check if all the values where sended and are not empty
    for field in required:

        # Check if field exist
        if field not in data:
            return jsonify({"message" : f"Missing '{field}' in the JSON"}), 400

        # Check if field is not empty
        if isinstance(data[field], str) and data[field] == "":
            return jsonify({"message" : f"The attribute '{field}' cannot be empty"}), 400
        if (isinstance(data[field], int) or isinstance(data[field], float)) and data[field] < 0:
            return jsonify({"message" : f"The attribute '{field}' cannot be lower than 0"}), 400

    # Get data from POST request
    name = data["name"]
    description = data["description"]
    price = data["price"]
    stock = data["stock"]

    # Connect to the DataBase
    cur = mysql.connection.cursor()

    # SQL Query
    try:
        cur.execute(f'UPDATE Product SET name = "{name}", description = "{description}", price = {price}, stock = {stock} WHERE idProduct = {product_id} AND User_idUser = {user_id}')

    # Catch Errors
    except:
        return jsonify({"message" : "Error inserting data in the DataBase, check your values!"}), 400

    # Save Changes in the DB
    mysql.connection.commit()

    # Return Updated Product
    return jsonify({
        "id" : product_id,
        "name" : name,
        "description" : description,
        "price" : price,
        "stock" : stock,
        "user_id" : user_id
        })


# * SERVICES ------------------------------------------------------------------------


# * SALES ---------------------------------------------------------------------------


# * CLIENTS -------------------------------------------------------------------------


# * End of backend
if __name__ == "__main__":
    app.run(debug = True, port = 5000)