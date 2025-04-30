from resources import postgre
from sqlalchemy import text
import pandas as pd
from resources.encrypt_pass import valid_pass
from resources.jwt import generate

postgre_uri =  'postgresql+psycopg2://app_user:app_user_2804222@127.0.0.1:5432/postgres'
con = postgre.Postgre(postgre_uri)

def valid_user_exist(email):
    return pd.read_sql_query(
        sql=text("""SELECT EXISTS(
                        SELECT  
                            1
                        FROM
                            personal_tasks.users
                        WHERE   
                            email = :email
                    )"""),
        params={"email": email},
        con=con.engine)['exists'][0]

def get_user_info(email):

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
        params={"email": email},
        con=con.engine
    )

def valid_user_password(user_info, passwd):

    if not user_info['active'][0]:
        return {"Error": "Inactive user"}

    encrypted_pass = user_info['password'][0]

    if not valid_pass(passwd, encrypted_pass):
        return {"Error": "Incorrect password"}

    return True