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