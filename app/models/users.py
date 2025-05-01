from resources import postgre
from sqlalchemy import text
import pandas as pd
from resources.encrypt_pass import valid_pass
import os

POSTGRE_URI = os.getenv('POSTGRE_URI_PRD')
class Users:

    def __init__(self, full_name, email, passwd):
        postgre_uri =  POSTGRE_URI

        self.full_name          = str(full_name)
        self.email              = str(email)
        self.passwd             = passwd
        self.postgre_connection = postgre.Postgre(postgre_uri)

    def __str__(self):
        return f'''
            "full_name": {self.full_name},
            "email":     {self.email},
            "password":  {self.passwd},
        '''

    def valid_user_exist(self):
        return pd.read_sql_query(
            sql=text("""SELECT EXISTS(
                            SELECT  
                                1
                            FROM
                                personal_tasks.users
                            WHERE   
                                email = :email
                        )"""),
            params={"email": self.email},
            con=self.postgre_connection.engine)['exists'][0]

    def get_user_info(self):
        return pd.read_sql_query(
            sql=text("""
                SELECT
                    id,
                    full_name,
                    email,
                    password,
                    active
                FROM personal_tasks.users
                WHERE email = :email
            """),
            params={"email": self.email},
            con=self.postgre_connection.engine
        )

    def valid_user_password(self, user_info):

        if not user_info['active'][0]:
            return {"Error": "Inactive user"}

        encrypted_pass = user_info['password'][0]

        if not valid_pass(self.passwd, encrypted_pass):
            return {"Error": "Incorrect password"}

        return True

    def create_user(self):
        '''This function is used to create a new user '''

        if self.valid_user_exist(self.email):
            return {"Error": "Email not available"}

        insert_user_query = f"""
            INSERT INTO personal_tasks.users(full_name, email, password, active)
            VALUES ('{self.full_name}', '{self.email}', '{self.passwd}', true)
        """

        try:
            self.postgre_connection.execute(insert_user_query)
            self.postgre_connection.connection.commit()
            return {"Message": "user created successfully"}, 200
        except Exception as e:
            return {"Error in insert new user": str(e)}, 400