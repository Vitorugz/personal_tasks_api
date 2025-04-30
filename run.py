from flask import Flask
from app import *

app = Flask(__name__)

app.register_blueprint(homepage_route)
app.register_blueprint(health_route)
app.register_blueprint(auth_route)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)