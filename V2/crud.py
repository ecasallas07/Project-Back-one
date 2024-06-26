from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from . import schemas
from . import models



# Users functions
def get_users(db:Session,limit: int = 100):
    try:
        obj=  db.query(models.User).limit(limit).all()
        return jsonable_encoder(obj)
    except Exception as e:
        return {'error':str(e)}


def get_user(db:Session,id:int):    
    obj = db.query(models.User).filter(models.User.id == id).first()
    if obj:
        return jsonable_encoder(obj)
    else:
        return None

def create_user(db:Session,user: schemas.User):
    try:
        db_user = models.User(username = user.username, email = user.email,first_name = user.first_name,lastname = user.lastname)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        return {'error':str(e)}
def update_user(db:Session,user: schemas.User,id:int):
    try:
        #  search user exist
        user = db.query(models.User).filer(models.User.id == id).first()
        
        if user:
            user.username = user.username
            user.email = user.email
            user.first_name = user.first_name
            user.last_name = user.last_name
            db.commit()
            db.refresh(user)
            return user
        else:
            return {"message":"User not found"}
    except Exception as e:
        return {'error':str(e)}    

def delete_user(db:Session,id:int):    
    try:
        user = db.query(models.User).filter(models.User.id == id).first()
        
        if user:
            db.delete(user)
            db.commit()
            return {"message":"User successfully deleted"}
    except Exception as e:
        return {'error':str(e)}    