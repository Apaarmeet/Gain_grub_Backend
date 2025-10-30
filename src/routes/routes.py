from fastapi import APIRouter, Depends, HTTPException
import jwt
from db.schema import UserCreate
from db.db import get_db,init_db
from db.models import User as UserModel
from db.schema import UserCreate
from sqlalchemy.orm import Session

User = APIRouter()




@User.get("/")
def root():
    return {
        "message": "Welcome"
   }
@User.post("/signup")
def signup(user_body: UserCreate, db: Session = Depends(get_db)):

    user_dict = user_body.model_dump()
    user_dict = user_body.model_dump()
    
    existing = db.query(UserModel).filter(UserModel.email == user_dict.get("email")).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = UserModel(**user_dict)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    payload = {
        "id": new_user.id,
        "username": user_dict["username"],
        "email": user_dict["email"],
    }
    token = jwt.encode(payload, "secret")

    return {
        "user": payload,
        "token": token
    }