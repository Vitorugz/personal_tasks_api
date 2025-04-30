from sqlalchemy import create_engine as _create_engine, text
from sqlalchemy.engine import Engine

class Postgre:

    def __init__(self, uri):
        self.uri             = uri
        self.engine          = self._get_engine()
        self._connection     = None

    def _get_engine(self) -> Engine:
        return _create_engine(self.uri)

    def __str__(self):
        return f"<Postgres: {self.engine}>"

    @property
    def connection(self):
        ''' Return a connection. '''

        if self._connection is None:
            self.connect()
        return self._connection

    def connect(self):
        ''' Connect to the database. '''

        self._connection = self.engine.connect()
        return self._connection

    def close(self):
        ''' Close the connection. '''

        if self._connection is not None:
            self._connection.close()
            self._connection = None

    def ping(self, if_error_raise: bool = False) -> bool:
        ''' Check if the connection is alive. '''

        try:
            self.execute('SELECT 1').fetchall()
            return True
        except Exception as exception:
            if if_error_raise:
                raise exception
            return False

    def execute(self, sql: str, *args, **kwargs):
        ''' Execute a SQL query and return the result if exists. '''

        if isinstance(sql, str):
            sql = text(sql)

        return self.connection.execute(sql, *args, **kwargs)

    def cursor(self, *args, **kwargs):
        ''' Return a cursor. '''

        return self.connection.connection.cursor(*args, **kwargs)
