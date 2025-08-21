from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import session
from typing import List
from database import engine,SessionLocal,Base
from models import Users
from schema import UserSchema,UserCreateSchema
from fastapi.responses import JSONResponse

Base.metadata.create_all(bind = engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
app = FastAPI()

@app.get("/users",response_model=List[UserSchema])
def get_data(db:session = Depends(get_db)):
    return db.query(Users).all()


@app.get("/users/{user_id}",response_model=UserSchema)
def get_by_id(user_id:int,db:session = Depends(get_db)):
    try:
        return db.query(Users).filter(Users.id == user_id).first()
    except:
        raise HTTPException(status_code=404, detail="user not found")

@app.post("/users",response_model=UserSchema)
def write_data(user:UserCreateSchema,db:session = Depends(get_db)):
    u = Users(name = user.name, password = user.password,email = user.email)
    db.add(u)
    db.commit()
    return u

@app.put("/users/{user_id}",response_model=UserSchema)
def update_user(user_id : int , user:UserSchema,db:session= Depends(get_db)):
    try:
        u = db.query(Users).filter(Users.id == user_id).first()
        u.name = user.name
        u.email = user.email
        db.add(u)
        db.commit()
        return u
    except:
        raise HTTPException(status_code=404, detail="User not Found")
    
@app.delete("/users/{user_id}",response_class=JSONResponse)
def delete_user(user_id: int, db:session = Depends(get_db)):
    try:
        u = db.query(Users).filter(Users.id == user_id).first()
        db.delete(u)
        db.commit()
        return {f"User of id {user_id} has been deleted":True}
    except:
        raise HTTPException(status_code=404, detail="User not Found")