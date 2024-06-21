from typing import Union
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from database import config
from database.config import DatabaseGateway
import json

app = FastAPI()

db_gateway = DatabaseGateway()

#USERS ENDPOINTS

class User(BaseModel):
    username: str
    email: str
    firsta_name: str
    lastname: str
@app.get("/blog")
def read_root():
    return{"message":"API project one BLOG"}
#Users router

@app.get("/blog/users")
def read_users():
    sql = "SELECT * FROM users"
    db = config.DatabaseGateway()
    try:
        info = db.db_query(sql)
        return {"user": info}
    except Exception as e:
        return {"error":str(e)}
     
@app.get("/blog/users/{id}") 
async def read_users_id(id: int):
   try:
       table_name = 'users'
       info = db_gateway.select_id(id,table_name)
       if info:
           user_info = json.loads(info)
           return {"user": user_info}
       else:
           raise HTTPException(status_code=404, detail="User not found")    
   except Exception  as e:
       return {'error':str(e)}
@app.post("/blog/users/save/")
def save_users(user: User):
    try:
        db =  db_gateway.db_connect()
        mycursor = db.cursor()
        query ="INSERT INTO users(username,email,firsta_name,lastname) VALUES (%s, %s, %s,%s)"
        data= (user.username,user.email,user.firsta_name,user.lastname)
        mycursor.execute(query,data)
        db.commit()
        return {"message": "User successfully added"}
    except Exception as e:
        return {'error':str(e)}

@app.put("/blog/users/edit/{id}")
async def edit_users(id:int,user:User):
    
    db= db_gateway.db_connect()
    try:
        mycursor=db.cursor()
        sql = "UPDATE users SET username = %s, email = %s,firsta_name= %s, lastname = %s WHERE id = %s"
        data = (user.username,user.email,user.firsta_name,user.lastname,id)
        mycursor.execute(sql,data)
        db.commit()
        if mycursor.rowcount > 0:
            return {"user":"User successfully updated"}
        else:
           raise HTTPException(status_code=404, detail="User no updated")   
    except Exception as e:
        return {"error": str(e)}     
    
@app.delete("/blog/users/delete/{id}")
def delete_users(id:int):
    db = db_gateway.db_connect()
    
    try:
        mycursor = db.cursor()
        sql = "DELETE FROM users WHERE id =  %s"
        mycursor.execute(sql,(id,))
        if mycursor.rowcount > 0:
            return {"user":"User seccessfully deleted"}
        else: 
            raise HTTPException(status_code=404, detail="User no deleted") 
    except Exception as e:
        return {"error": str(e)}    
# ARTICLES ENDPOINTS
@app.get("/blog/articles")
def read_articles():
    sql = "SELECT * FROM articles"
    db =  config.DatabaseGateway()
    try:
        info = db.db_query(sql)
        return {"articles": info}
    except Exception as e:
        return {'error': str(e)}
            
@app.get("/blog/articles/{id}")
def read_articles_id(id:int):

    try:
        db_gateway.select_id(id,'articles')

    except Exception as e:
        return {'error':str(e)}








