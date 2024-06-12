import mysql.connector
import json

class DatabaseGateway:

    def db_connect(self):
        db_con = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password  = "4577",
                database = "blog_api"
                )
        cursor = db_con.cursor()
        cursor.execute("SELECT DATABASE()")
        data = cursor.fetchone()
        print("Connection established to: ",data)
        return db_con

    def db_query(self,query_string):

        my_db = self.db_connect()
        mycursor = 
