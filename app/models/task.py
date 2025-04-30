from resources import postgre
from sqlalchemy import text
import pandas as pd

class Taks:

    def __init__(self, title, desc):
        postgre_uri =  'postgresql+psycopg2://app_user:app_user_2804222@127.0.0.1:5432/postgres'

        self.title = title
        self.desc  = desc
        self.postgre_connection = postgre.Postgre(postgre_uri)

    def create_taks(self, user_id):
        ''' This function is used to create a new task '''