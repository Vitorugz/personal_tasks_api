from flask import Blueprint, request
from ..models.users import Users
from resources.encrypt_pass import encrypt_password
from resources import jwt as _jwt
from resources.mail import Mail

auth_route = Blueprint('auth', __name__)

@auth_route.post("/register")
def register_user():
    ''' This function is used to create a new user '''
    try:

        if 'name' not in request.json:
            return {"Error": "Please, inform the full name!"}, 400
        elif 'password' not in request.json:
            return {"Error": "Please, inform the password!"}, 400
        elif 'email' not in request.json:
            return {"Error": "Please, informe the email!"}, 400
        
        full_name = request.json['name']
        email     = request.json['email']
        passwd    = request.json['password']

        user = Users(full_name, email, encrypt_password(passwd))

        create_user = user.create_user()

        if 'Error' in create_user:
            return create_user

        mail = Mail()

        mail.send(email, "Welcome to the API", "You have successfully registered in the API")

        return create_user
    except Exception as e:
        return {"Error": str(e)}

@auth_route.post("/login")
def login():
    ''' Validate the received body and return a JWT Token to the user '''

    try:

        if 'email' not in request.json:
            return {"Error": "Please, inform your e-mail!"}, 400
        elif 'password' not in request.json:
            return {"Error": "Please, inform yout password"}, 400

        email = request.json['email']
        passwd = request.json['password']

        user = Users('', email, passwd)

        if not user.valid_user_exist():
            return {"Error": "User not found"}

        user_info = user.get_user_info()

        valid_user = user.valid_user_password(user_info)

        if valid_user != True:
            return valid_user

        jwt = _jwt.generate_jwt(str(user_info['email'][0]), str(user_info['full_name'][0]), str(user_info['id'][0]))

        user.update_last_login_date(user_info['id'][0])

        return {"access_token": jwt}, 200

    except Exception as e:
        return {"Error": str(e)}