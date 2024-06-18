from typing import Union
from fastapi import FastAPI
from database import config

app = FastAPI()

@app.get("/hee")
def read_root():
    return{"message":"API project one BLOG"}

@app.get("/users")
def read_users():
    sql = "SELECT * FROM users"
    db = config.DatabaseGateway()
    try:
        info = db.db_query(sql)
        #return {"user": info}
    except Exception as e:
        return {"error":str(e)}
     
@app.get("/users/{id}") 
def read_users_id(id: int):
   #sql  = "SELECT * FROM users WHERE id '" + str(id) +"'" 
   #db = config.DatabaseGateway()
   try:
      config.select_id(id,'users')     
   except Exception  as e:
       return {'error':str(e)}


@app.get("/articles")
def read_articles():
    sql = "SELECT * FROM articles"
    db =  config.DatabaseGateway()
    try:
        info = db.db_query()
    except Exception as e:
        return {'error': str(e)}
            
@app.get("/articles/{id}")
def read_articles_id(id:int):
    #db =  config.DatabaseGateway()
    try:
        coonfig.select_id(id,'articles')

    except Exception as e:
        return {'error':str(e)}








