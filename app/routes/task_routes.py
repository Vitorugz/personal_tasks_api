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

@task_route.get("/tasks/getAllTasks")
@requires_auth
def get_tasks():
    ''' This function is used to get all tasks of a user '''

    jwt = request.headers.get('Authorization')

    user_info = decode_jwt(jwt)

    tasks = []

    task = Task('', '', user_info['id_user'])

    for row in task.get_tasks().itertuples():
        tasks.append({
            "title": row.title,
            "description": row.description
        })

    return tasks

@task_route.delete("/task/delete")
@requires_auth
def delete_task():

    jwt = request.headers.get('Authorization')
    task_id = request.args.get('task_id')

    if not task_id:
        return {"Error": "Please, informe task_id"}, 400

    user_info = decode_jwt(jwt)

    task = Task('', '', user_info['id_user'])

    return task.delete_task(task_id)
