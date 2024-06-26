from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True,autoincrement=True)
    username = Column(String(50), default ='User00000')
    email= Column(String(60),unique=True,index=True)
    first_name= Column(String(50))
    lastname = Column(String(50))
    
    articles = relationship("Article",back_populates="owner")

class Article(Base):
    __tablename__ = "articles"
    
    id = Column(Integer, primary_key=True,autoincrement=True)
    title = Column(String(40),unique=True)
    content = Column(String(255))
    summary = Column(String(150))
    status = Column(Integer)
    created_at = Column(DateTime,default =func.now)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship("User",back_populates="articles")
    
class Category(Base): 
    __tablename__ = "category"
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(70))
    description = Column(String(255))


class Article_Category(Base):
    __tablename__ = "article_category"
    article_id = Column(Integer,primary_key=True)
    category_id = Column(Integer,primary_key=True)
    
    