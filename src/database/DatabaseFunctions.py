import sqlite3
from sqlite3 import Error

class DBInteractions:

    conn = None

    def __init__(self):
        database = "C:\\sqlite\db\pythonsqlite.db"
        self.conn = self.create_connection(database)
        with self.conn:
            pass

    def create_connection(self, db_file):
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return None

    def getPeople(self, max=100, sortCriteria=None, searchCriteria=None):
        cur = self.conn.cursor()

        #TODO Sanitize SQL inputs

        statement = "SELECT * FROM users LIMIT " + str(max)
        if sortCriteria:
            statement += " ORDER BY " + sortCriteria
        if searchCriteria:
            statement += " WHERE Phone LIKE " + searchCriteria + " OR Email LIKE " + searchCriteria
        statement += " ;"

        cur.execute(statement)

        rows = cur.fetchall()

        for row in rows:
            yield(row)



