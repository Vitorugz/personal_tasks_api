from flask import Blueprint

health_route = Blueprint('health', __name__)

@health_route.get("/health")
def health():
    ''' Returns a simple JSON to report the current status of the API '''
    return {"API Status": "Active"}, 200

@health_route.get("/health/database")
def health_database():
    ''' Returns a simple JSON to report the current status of the database connection '''

    return {"DB Status": "Not connected"}, 500