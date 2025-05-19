from resources import postgre
from sqlalchemy import text
import pandas as pd
import os

class Task:

    def __init__(self, title, desc, user_id):

        self.title              = title
        self.desc               = desc
        self.user_id            = user_id
        self.postgre_connection = postgre.Postgre()

    def create_taks(self):
        ''' This function is used to create a new task '''
        insert_user_query = f"""
            INSERT INTO task(title, description, user_task)
            VALUES ('{self.title}', '{self.desc}', '{self.user_id}')
        """

        try:
            self.postgre_connection.execute(insert_user_query)
            self.postgre_connection.connection.commit()
            return {"Message": "Task created successfully"}, 200
        except Exception as e:
            return {"Error in insert new task": str(e)}, 400

    def get_tasks(self):
        ''' This function is used to get all tasks of a user '''
        return pd.read_sql_query(
            sql=text("""SELECT * FROM task WHERE user_task = :user_id"""),
            params={"user_id": self.user_id},
            con=self.postgre_connection.engine
        )

    def find_task(self, task_id, user_id, engine):
        ''' This function is used to valid if task exist '''
        return pd.read_sql_query(
            sql=text("""
            SELECT EXISTS (
                SELECT
                    1
                FROM task
                WHERE id        = :task_id
                AND   user_task = :user_id
            )
        """),
        params={"task_id": task_id, "user_id": user_id},
        con=engine
        )['exists'][0]

    def delete_task(self, task_id):
        ''' This function is used to delete a task '''

        if not self.find_task(task_id, self.user_id, self.postgre_connection.engine):
            return {"Error": "Task not found for your user!"}
        delete_task_query = f"""
            DELETE FROM task
            WHERE id        = {task_id}
            AND   user_task = {self.user_id}
        """

        try:
            self.postgre_connection.execute(delete_task_query)
            self.postgre_connection.connection.commit()
            return {"Message": "Task deleted successfully"}, 200
        except Exception as e:
            return {"Error in delete task": str(e)}, 400

    def update_fields(self, task_id, fields):
        try:
            # Exemplo usando SQL diretamente (adaptar conforme seu ORM ou método atual)
            set_clause = ", ".join([f"{key} = %s" for key in fields.keys()])
            values = list(fields.values())

            sql = f"UPDATE tasks SET {set_clause} WHERE id = %s AND user_id = %s"
            values.append(task_id)
            values.append(self.user_id)

            # executar a query com seus métodos usuais
            self.postgre_connection.execute(sql, values)
            self.postgre_connection.connection.commit()
            return {"Message": "Task updated successfully"}
        except Exception as e:
            return {"Error": str(e)}, 500

    def update_task_title(self, task_id):
        ''' This function is used to update a task title '''
        if not self.find_task(task_id, self.user_id, self.postgre_connection.engine):
            return {"Error": "Task not found!"}
        update_title_task_query = f"""UPDATE task SET title = '{self.title}' WHERE id  = {task_id}"""

        try:
            self.postgre_connection.execute(update_title_task_query)
            self.postgre_connection.connection.commit()
            return {"Message": "Task Title Updated successfully!"}, 200
        except Exception as e:
            return {"Error in update task title": str(e)}, 400
        
    def update_task_desc(self, task_id):
        ''' This function is used to update a task description '''
        if not self.find_task(task_id, self.user_id, self.postgre_connection.engine):
            return {"Error": "Task not found!"}
        update_title_task_query = f"""
            UPDATE task 
            SET description = '{self.desc}'
            WHERE id  = {task_id}
        """

        try:
            self.postgre_connection.execute(update_title_task_query)
            self.postgre_connection.connection.commit()
            return {"Message": "Task Description Updated successfully!"}, 200
        except Exception as e:
            return {"Error in update task description": str(e)}, 400
        
    def update_task_status(self, task_id, task_status):
        ''' This function is used to update a task status '''
        if not self.find_task(task_id, self.user_id, self.postgre_connection.engine):
            return {"Error": "Task not found!"}

        update_title_task_query = f"""
            UPDATE task 
            SET status = {task_status}
            WHERE id  = {task_id}
        """

        try:
            self.postgre_connection.execute(update_title_task_query)
            self.postgre_connection.connection.commit()
            return {"Message": "Task Status Updated successfully!"}, 200
        except Exception as e:
            return {"Error in update task Status": str(e)}, 400