import jwt
from datetime import datetime, timedelta, timezone

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
        jwt_decode_token = jwt.decode(jwt_token, '4EYRgmUKOYjLRY0Xu6otDf2IVbr4XAHUoYnTDTy6JWM=', "HS256")
        return jwt_decode_token
    
    except jwt.ExpiredSignatureError:
        return {
            "Erro": "Token Expirou"
        }

    except jwt.InvalidTokenError:
        return {
            "Erro": "Token Inválido"
        }
