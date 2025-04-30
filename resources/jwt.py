import jwt
from datetime import datetime, timedelta, timezone

def decode_jwt(token):
    jwt_decoded = jwt.decode(token, '4EYRgmUKOYjLRY0Xu6otDf2IVbr4XAHUoYnTDTy6JWM=', "HS256")
    return jwt_decoded

# This functions is used to generate a JWT.
def generate(email, full_name, id):

    payload = {
        "email": email,
        "full_name": full_name,
        "id_user": id,
        'exp': (datetime.now(timezone.utc) + timedelta(hours=1))
    }

    jwt_token = jwt.encode(payload, '4EYRgmUKOYjLRY0Xu6otDf2IVbr4XAHUoYnTDTy6JWM=', "HS256")

    return jwt_token

# This functions is used to validate a JWT.
def validate(jwt_token):
    try:
        decode_jwt(jwt_token)
        return {
            "Success": "Valid token!"
        }
    except jwt.ExpiredSignatureError:
        return {
            "Error": "Token Expirou"
        }

    except jwt.InvalidTokenError:
        return {
            "Error": "Token Inválido"
        }
