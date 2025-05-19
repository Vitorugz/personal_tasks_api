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

    if "Error" in user_info:
        return user_info

    task = Task(task_title, task_desc, user_info['id_user'])

    return task.create_taks()

@task_route.get("/task/getAllTasks")
@requires_auth
def get_tasks():
    ''' This function is used to get all tasks of a user '''

    jwt = request.headers.get('Authorization')

    user_info = decode_jwt(jwt)

    if "Error" in user_info:
        return user_info

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

    if "Error" in user_info:
        return user_info

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
    if "Error" in user_info:
        return user_info

    data = request.json
    if not data:
        return {"Error": "Please, inform any field to change"}, 400

    allowed_fields = ['title', 'description', 'status']
    fields_to_update = {k: v for k, v in data.items() if k in allowed_fields}

    if not fields_to_update:
        return {"Message": "No valid fields provided to update"}, 400

    task = Task(
        title=fields_to_update.get('title', ''),
        description=fields_to_update.get('description', ''),
        user_id=user_info['id_user']
    )

    return task.update_fields(task_id, fields_to_update)
