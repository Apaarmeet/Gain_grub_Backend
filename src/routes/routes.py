from fastapi import APIRouter
from pydantic import BaseModel
import jwt
from db.schema import UserCreate

User = APIRouter()




@User.get("/")
def root():
    return {
        "message": "Welcome"
   }

@User.post("/signup")
def signup(user_body: UserCreate):


    user_dict = user_body.model_dump()
    payload = {
        "username": user_dict["username"],
        "email": user_dict["email"],
    }
    token = jwt.encode(payload, "secret")

    return {
        "user": payload,
        "token": token
    }