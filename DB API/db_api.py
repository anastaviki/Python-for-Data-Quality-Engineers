import pyodbc


class DatabaseApi:  # class for working with db
    def __init__(self):  # create connection and cursor here
        self.query = ""
        with pyodbc.connect('DRIVER={SQLite3 ODBC Driver};Direct=True;'
                            'Database=newsfeed.db;String Types= Unicode', autocommit=True) as self.connection:
            with self.connection.cursor() as self.cursor:
                pass

    def create_table(self, name, fields):  # function for creating table, in fields we determine name and datatype
        self.query = f"CREATE TABLE IF NOT EXISTS {name} ("
        for key, value in fields.items():
            self.query = self.query + key + " " + value + ","
        self.query = self.query[:-1]
        self.query = self.query + ");"
        self.cursor.execute(self.query)

    def insert_into_table(self, name, values):  # function for inserting row if it is not exists
        self.query = f"INSERT INTO {name}("
        for i in values:
            self.query = self.query + i[0] + ", "
        self.query = self.query[:-2] + ") Select "
        for i in values:
            self.query = self.query + "'"+i[1] + "', "
        self.query = self.query[:-2] + f" WHERE NOT EXISTS(SELECT * FROM {name} WHERE "
        for i in values:
            self.query = self.query + f" {i[0]} = '{i[1]}' AND "
        self.query = self.query[:-4] + ");"

        self.cursor.execute(self.query)
