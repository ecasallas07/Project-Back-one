from typing import Union
from pydantic import BaseModel


class User(BaseModel): 
    username: str
    email:str
    first_name: str
    lastname: str
    
class Article(BaseModel): 
    title: str
    content: str
    summary: str
    status: int
    user_id: int   
    
class Crategory(BaseModel): 
    name: str
    description: str     