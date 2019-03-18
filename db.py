import sqlite3

class DBHandler(object):
    __instance = None

    @staticmethod
    def getInstance():        
        """ Static access method. """
        if DBHandler.__instance == None:
            DBHandler()
        return DBHandler.__instance 

    def __init__(self):
        """ Virtually private constructor. """
        if DBHandler.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            self.conn = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
            self.conn.row_factory = sqlite3.Row            
            DBHandler.__instance = self
            with open('schema.sql', 'r') as file:
                self.conn.executescript("".join(file.readlines()))

    def commitExecution(self, query, parameters):
        """ Execute an SQL insert, update or select statement
            with the dbconnector """
        cur = self.conn.cursor()
        try:
            cur.execute(query, parameters)
            self.conn.commit()
            return cur.lastrowid
        except Exception as e:
            print(e)
            self.conn.rollback()
        finally:
            cur.close()
            
    def fetchOneExecution(self, query, parameters):
        """ Execute an SQL select statement with the db connector 
            and returns only the first row """
        cur = self.conn.cursor()
        try:
            cur.execute(query, parameters)
            return cur.fetchone()
        finally:
            cur.close()

    def fetchAllExecution(self, query, parameters = None):
        """ Execute an SQL select statement with the db connector
            and returns all rows """
        cur = self.conn.cursor()
        try:
            if parameters == None:
                cur.execute(query)
            else:
                cur.execute(query, parameters)
            return cur.fetchall()
        finally:
            cur.close()
            
    def close(self):
        self.conn.close()
