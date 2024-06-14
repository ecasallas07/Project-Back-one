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
        return {"user": info}
    except Exception as e:
        return {"error":str(e)}
     


#@app.get("/articles"):






