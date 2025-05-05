from ..models.task import Task
from flask import Blueprint, request
from resources.jwt import decode_jwt
from ..decorators.valid_login import requires_auth

task_route = Blueprint('task', __name__)

@task_route.post("/task/create")
@requires_auth
def create_task():
    ''' This function is used to create a new task '''

    jwt = request.headers.get('Authorization')

    if 'title' not in request.json:
        return {"Error": "Plase, inform the title"}
    elif 'description' not in request.json:
        return {"Error": "Plase, inform the description"}

    task_title = request.json['title']
    task_desc  = request.json['description']

    user_info = decode_jwt(jwt)

    task = Task(task_title, task_desc, user_info['id_user'])

    return task.create_taks()

@task_route.get("/task/getAllTasks")
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
            "description": row.description,
            "task_id": row.id,
            "task_status": row.status
        })

    return tasks

@task_route.delete("/task/delete")
@requires_auth
def delete_task():
    ''' This function is used to delete a task '''

    jwt = request.headers.get('Authorization')
    task_id = request.args.get('task_id')

    if not task_id:
        return {"Error": "Please, informe task_id"}, 400

    user_info = decode_jwt(jwt)

    task = Task('', '', user_info['id_user'])

    return task.delete_task(task_id)

@task_route.put("/task/update")
@requires_auth
def update_task():
    ''' This function is used to update a task '''

    jwt = request.headers.get('Authorization')
    task_id = request.args.get('task_id')

    if not task_id:
        return {"Error": "Please, informe task_id"}, 400
    
    user_info = decode_jwt(jwt)

    if 'title' in request.json:
        task = Task(request.json['title'], '', user_info['id_user'])
    
        return task.update_task_title(task_id)
    if 'description' in request.json:
        task = Task('', request.json['description'], user_info['id_user'])
    
        return task.update_task_desc(task_id)

    if 'status' in request.json:
        task = Task('', '', user_info['id_user'])
    
        return task.update_task_status(task_id, request.json['status'])

    else:
        return {"Message": "Please, inform any field to change"}, 400