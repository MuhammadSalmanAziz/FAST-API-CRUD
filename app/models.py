from database import Base
from sqlalchemy import Integer,String, Column

class Users(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True,index = True)
    name = Column(String(50))
    email = Column(String(100),unique=True)
    password = Column(String(20))