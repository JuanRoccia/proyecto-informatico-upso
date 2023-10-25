# Decoradores
from extensions import app
from functools import wraps
from flask import request, jsonify
import jwt
from extensions import app

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
