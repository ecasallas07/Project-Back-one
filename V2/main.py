from fastapi import  Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, schemas
from . import models
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db # yield allow create dependencies --> es generadora de sessiones en la base de datos 
    finally:
        db.close()
        
# ENDPOINT USERS
        
@app.get("/V2/blog/users",response_model =list[schemas.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db,limit=limit)
    return users


@app.get("/V2/blog/users/{id}")
def get_user(id:int,db: Session = Depends(get_db)):
    user = crud.get_user(db,id=id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/V2/blog/users/create/")
def create_user(user: schemas.User,db:Session = Depends(get_db)):
    user = crud.create_user(db,user)
    return user

@app.put("/V2/blog/users/edit/{id}")
def edit_user(user:schemas.User,id:int,db: Session = Depends(get_db)):
    user = crud.update_user(db,user,id)
    return user

@app.delete("/V2/blog/users/delete/{id}")
def  delete_user(id:int,db: Session = Depends(get_db)):
    user = crud.delete_user(db,id)
    return user



# ENDPOINT ARTICLES
@app.get("/V2/blog/users",response_model =list[schemas.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db,limit=limit)
    return users


@app.get("/V2/blog/users/{id}")
def get_user(id:int,db: Session = Depends(get_db)):
    user = crud.get_user(db,id=id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/V2/blog/users/create/")
def create_user(user: schemas.User,db:Session = Depends(get_db)):
    user = crud.create_user(db,user)
    return user

@app.put("/V2/blog/users/edit/{id}")
def edit_user(user:schemas.User,id:int,db: Session = Depends(get_db)):
    user = crud.update_user(db,user,id)
    return user

@app.delete("/V2/blog/users/delete/{id}")
def  delete_user(id:int,db: Session = Depends(get_db)):
    user = crud.delete_user(db,id)
    return user