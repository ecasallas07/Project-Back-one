import mysql.connector
import json

class DatabaseGateway:

    def db_connect(self):
        db_con = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password  = '4577',
                database = 'blog_api'
                )
        cursor = db_con.cursor()
        cursor.execute("SELECT DATABASE()")
        data = cursor.fetchone()
        if data:
            print("Connection established to: ",data[0])
        else:
            print("Connection error")
        return db_con

    def db_query(self,query_string):
        if self.db_connect() is None:
            raise Exception("No se puede realizar la consulta.")

        my_db= self.db_connect()
        mycursor= my_db.cursor() 
        mycursor.execute(query_string)


        columnas = mycursor.description
        data= []

        for row in mycursor.fetchall():
            row_data = {}
            for(column_name,column_value) in enumerate(row):
                row_data[columnas[column_name][0]] = column_value

            data.append(row_data)
            
        return data
        # json_object = json.dumps(data) # dumps: convert data to json

        # return json_object


    def db_execute(self, query_string,data):
        my_db = self.db_connect()
        mycursor  = my_db.cursor()
        mycursor.execute(query_string,data)
        my_db.commit() # save changes in database

        self.lastrowid = str(mycursor.lastrowid) # lastrowid recuperate the id of last row
        print(f"Elemento guardado con el id: {self.lastrowid}")     

    def select_id(self,id,table):
        db = self.db_connect()
        if db is None:
            return None
        try:
            mycursor = db.cursor(dictionary=True)
            sql =f"SELECT * FROM {table} WHERE id = %s"
            mycursor.execute(sql, (id,)) #la coma es una convecion de python para decir q es una tupla de un solo elemento 
            result = mycursor.fetchone()
            return json.dumps(result)
        except Exception as e:
            return {'error':str(e)}
# Test connection database
w1 = DatabaseGateway()
w1.db_connect()


        
