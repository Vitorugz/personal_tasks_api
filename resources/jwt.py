import jwt
from datetime import datetime, timedelta, timezone
import os

JWT_KEY = os.getenv('JWT_KEY')

def decode_jwt(token):
    ''' This function is used to decode a JWT Token'''
    jwt_decoded = jwt.decode(token, JWT_KEY, "HS256")
    return jwt_decoded

# This functions is used to generate a JWT.
def generate_jwt(email, full_name, id):
    ''' This function is used to generate a JWT Token '''

    payload = {
        "email": email,
        "full_name": full_name,
        "id_user": id,
        'exp': (datetime.now(timezone.utc) + timedelta(hours=1))
    }

    jwt_token = jwt.encode(payload, JWT_KEY, "HS256")

    return jwt_token

# This functions is used to validate a JWT.
def validate_jwt(jwt_token):
    ''' This Functions is used to valid a JWT Token'''

    try:
        jwt_decoded = jwt.decode(jwt_token, JWT_KEY, "HS256")
        return jwt_decoded
    except jwt.exceptions.ExpiredSignatureError:
        return {
            "Error": "Token Expirado"
        }
    except jwt.exceptions.InvalidTokenError:
        return {
            "Error": "Token Inválido"
        }