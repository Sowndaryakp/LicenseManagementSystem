# backend/app/api/auth.py

from fastapi import APIRouter, HTTPException
from db.models import User
from pony.orm import db_session

router = APIRouter()

@router.post("/register/")
@db_session
def register(email: str, password: str, company: str, username: str):
    user = User.get(email=email)
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = User(email=email, password=password, company=company, username=username)
    return {"message": "Registered successfully"}

@router.post("/login/")
@db_session
def login(email: str, password: str):
    user = User.get(email=email, password=password)
    if user:
        return {"message": "Logged in successfully", "isAdmin": user.isAdmin}
    raise HTTPException(status_code=401, detail="Invalid email or password")
