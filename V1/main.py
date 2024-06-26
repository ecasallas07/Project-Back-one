# from typing import Union
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from database import config
from database.config import DatabaseGateway
import json

app = FastAPI()

db_gateway = DatabaseGateway()
DB = db_gateway.db_connect()

class User(BaseModel):
    username: str
    email: str
    firsta_name: str
    lastname: str
    
class Article(BaseModel):    
    title:str
    content: str
    summary: str
    status: int
    user_id: int 

class Category(BaseModel):
    name: str
    description: str
    
class Articles_Category(BaseModel):
    article_id: int
    category_id: int
@app.get("/V1/blog")
def read_root():
    return{"message":"API project one BLOG"}

#USERS ENDPOINTS
@app.get("/V1/blog/users")
def read_users():
    sql = "SELECT * FROM users"
    try:
        info = DB.db_query(sql)
        return {"user": info}
    except Exception as e:
        return {"error":str(e)}
     
@app.get("/V1/blog/users/{id}") 
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
@app.post("/V1/blog/users/save/")
def save_users(user: User):
    try:
        mycursor = DB.cursor()
        query ="INSERT INTO users(username,email,firsta_name,lastname) VALUES (%s, %s, %s,%s)"
        data= (user.username,user.email,user.firsta_name,user.lastname)
        mycursor.execute(query,data)
        DB.commit()
        return {"message": "User successfully added"}
    except Exception as e:
        return {'error':str(e)}

@app.put("/V1/blog/users/edit/{id}")
async def edit_users(id:int,user:User):
    try:
        mycursor=DB.cursor()
        sql = "UPDATE users SET username = %s, email = %s,firsta_name= %s, lastname = %s WHERE id = %s"
        data = (user.username,user.email,user.firsta_name,user.lastname,id)
        mycursor.execute(sql,data)
        DB.commit()
        if mycursor.rowcount > 0:
            return {"user":"User successfully updated"}
        else:
           raise HTTPException(status_code=404, detail="User no updated")   
    except Exception as e:
        return {"error": str(e)}     
    
@app.delete("/V1/blog/users/delete/{id}")
def delete_users(id:int):
    try:
        mycursor = DB.cursor()
        sql = "DELETE FROM users WHERE id =  %s"
        mycursor.execute(sql,(id,))
        DB.commit()  # commit() --> save changes to database
        if mycursor.rowcount > 0:
            return {"user":"User seccessfully deleted"}
        else: 
            raise HTTPException(status_code=404, detail="User no deleted") 
    except Exception as e:
        return {"error": str(e)}    
    
# ARTICLES ENDPOINTS
@app.get("/V1/blog/articles")
def read_articles():
    sql = "SELECT * FROM articles"  
    try:
        info = DB.db_query(sql)
        return {"articles": info}
    except Exception as e:
        return {'error': str(e)}
            
@app.get("/V1/blog/articles/{id}")
def read_articles_id(id:int):
    try:
        info = db_gateway.select_id(id,'articles')
        
        if info:
            article_info = json.loads(info)
            return {"article": article_info}
        else:
            raise HTTPException(status_code=404, detail="User not found") 

    except Exception as e:
        return {'error':str(e)}

@app.post("/V1/blog/articles/save/")
def save_articles(article:Article):
    try:
        mycursor = DB.cursor()
        sql = "INSERT INTO articles(title,content,summary,status,user_id) VALUES(%s,%s,%s,%s,%s)"
        data = (article.title,article.content,article.summary, article.staus,article.user_id)
        mycursor.execute(sql,data)
        DB.commit()
        if mycursor.rowcount > 0:
            return {"message":"Article succeessfully added"}
    except Exception as e:
        return {"error":str(e)}

@app.put("/V1/blog/articles/edit/{id}")
def edit_articles(id:int,article:Article):

    try:
        mycursor = DB.cursor()
        sql = "UPDATE articles SET title = %s, content = %s, summary = %s, status = %s, user_id = %s WHERE id = %s"
        data = (article.title,article.content,article.summary,article.status,article.user_id,id)
        mycursor.execute(sql,data)
        DB.commit()
        if mycursor.rowcount > 0:
            return {"article":"Article successfully updated"}
        else:
           raise HTTPException(status_code=404, detail="Article no updated")
    except Exception as e:
        return {'error': str(e)}    


@app.delete("/V1/blog/articles/delete/{id}")
def delete_articles(id:int):
    
    try:
        mycursor = DB.cursor()
        sql = "DELETE FROM articles WHERE id = %s"
        mycursor.execute(sql,(id,))
        DB.commit()
        
        if mycursor.rowcount > 0:
            return {"message":"Article successfully deleted"}
    except Exception as e:
        return {"error":str(e)}

    

# CATEGORY ENDPOINTS
@app.get("/V1/blog/category")
def read_category():
    sql = "SELECT * FROM category"
    try:
        info = DB.db_query(sql)
        return {"category": info}
    except Exception as e:
        return {"error":str(e)}
     
@app.get("/V1/blog/category/{id}") 
async def read_category_id(id: int):
   try:
       info = db_gateway.select_id(id,'category')
       if info:
           category_info = json.loads(info)
           return {"category": category_info}
       else:
           raise HTTPException(status_code=404, detail="Category not found")    
   except Exception  as e:
       return {'error':str(e)}
@app.post("/V1/blog/category/save/")
def save_category(category: Category):
    try:
        mycursor = DB.cursor()
        query ="INSERT INTO category(title,content,summary,status,user_id) VALUES (%s, %s, %s,%s,%s)"
        data= (category.title,category.content,category.summary,category.status,category.user_id)
        mycursor.execute(query,data)
        DB.commit()
        return {"message": "User successfully added"}
    except Exception as e:
        return {'error':str(e)}

@app.put("/V1/blog/category/edit/{id}")
async def edit_category(id:int,category:Category):
    try:
        mycursor=DB.cursor()
        sql = "UPDATE category SET title = %s, content = %s,summary= %s, status = %s, user_id = %s WHERE id = %s"
        data = (category.title,category.content,category.summary,category.status,category.user_id)
        mycursor.execute(sql,data)
        DB.commit()
        if mycursor.rowcount > 0:
            return {"user":"Category successfully updated"}
        else:
           raise HTTPException(status_code=404, detail="Category no updated")   
    except Exception as e:
        return {"error": str(e)}     
    
@app.delete("/V1/blog/category/delete/{id}")
def delete_category(id:int):
    try:
        mycursor = DB.cursor()
        sql = "DELETE FROM category WHERE id =  %s"
        mycursor.execute(sql,(id,))
        DB.commit()  # commit() --> save changes to database
        if mycursor.rowcount > 0:
            return {"user":"Category seccessfully deleted"}
        else: 
            raise HTTPException(status_code=404, detail="Category no deleted") 
    except Exception as e:
        return {"error": str(e)}    




