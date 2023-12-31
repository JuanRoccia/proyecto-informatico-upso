# Utilidades
import hashlib, base64

def encode_password(password, seed):
    # Encode password with seed using PBKDF2
    # PBKDF2 is a key derivation function that generates a key from a password and a salt
    # The key is generated by applying the hash function to the password and the salt
    # The hash function is SHA256
    b_seed = seed.encode('utf-8')
    b_password = password.encode('utf-8')
    encoded_password = hashlib.pbkdf2_hmac('sha256', b_password, b_seed, 100000)
    encoded_password_b64 = base64.b64encode(encoded_password).decode('utf-8')
    return encoded_password_b64

def validate_data(data,required):
    # Check if all the values where sended and are not empty
    for field in required:

        # Check if field exist
        if field not in data:
            return False, f"Missing '{field}' in the JSON!"

        # Check if str field is not empty
        if isinstance(data[field], str) and data[field] == "":
            return False, f"The attribute '{field}' cannot be empty!"

        # Check if int/float field is not lower than 0
        if (isinstance(data[field], int) or isinstance(data[field], float)) and data[field] < 0:
            return False, f"The attribute '{field}' cannot be lower than 0!"

        # Check if list of id contains only integers
        if isinstance(data[field], list):
            # Iterate in the list to check each value
            for ids in data[field]:
                if not isinstance(ids, int):
                    return False, f"Only ID's allowed in the list!"

    return True, None