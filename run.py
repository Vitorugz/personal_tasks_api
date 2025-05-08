from app import *
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.register_blueprint(auth_route)
app.register_blueprint(task_route)
app.register_blueprint(homepage_route)

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )