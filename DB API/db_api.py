import pyodbc

class DatabaseApi:
    def __init__(self):
        with pyodbc.connect('DRIVER={SQLite3 ODBC Driver};Direct=True;'
                            'Database=newsfeed.db;String Types= Unicode') as self.connection:
            with self.connection.cursor() as self.cursor:
                pass
    def create_table(self):
        self.cursor.execute('Create')

