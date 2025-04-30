from flask import Blueprint, request
from ..decorators.valid_login import requires_auth
from resources.jwt import decode_jwt
from ..models.task import Task

task_route = Blueprint('task', __name__)

@task_route.post("/tasks/create")
@requires_auth
def create_task():
    ''' This function is used to create a new task '''

    jwt = request.headers.get('Authorization')
    task_title = request.json['title']
    task_desc  = request.json['description']

    user_info = decode_jwt(jwt)

    task = Task(task_title, task_desc, user_info['id_user'])

    return task.create_taks()

    return {
        "User_task":        user_info['id_user'],
        "Name_user_task":   user_info['full_name'],
        "Task_title":       task_title,
        "Task_description": task_desc
    }