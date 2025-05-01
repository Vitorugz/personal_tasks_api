from resources import postgre
from sqlalchemy import text
import pandas as pd

class Task:

    def __init__(self, title, desc, user_id):
        postgre_uri =  'postgresql+psycopg2://app_user:app_user_2804222@127.0.0.1:5432/postgres'

        self.title              = title
        self.desc               = desc
        self.user_id            = user_id
        self.postgre_connection = postgre.Postgre(postgre_uri)

    def create_taks(self):
        ''' This function is used to create a new task '''

        insert_user_query = f"""
            INSERT INTO personal_tasks.task(title, description, user_task)
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
            sql=text("""SELECT * FROM personal_tasks.task WHERE user_task = :user_id"""),
            params={"user_id": self.user_id},
            con=self.postgre_connection.engine
        )

    def find_task(self, task_id, user_id, engine):

        return pd.read_sql_query(
            sql=text("""
            SELECT EXISTS (
                SELECT
                    1
                FROM personal_tasks.task
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
            DELETE FROM personal_tasks.task
            WHERE id        = {task_id}
            AND   user_task = {self.user_id}
        """

        try:
            self.postgre_connection.execute(delete_task_query)
            self.postgre_connection.connection.commit()
            return {"Message": "Task deleted successfully"}, 200
        except Exception as e:
            return {"Error in delete task": str(e)}, 400

