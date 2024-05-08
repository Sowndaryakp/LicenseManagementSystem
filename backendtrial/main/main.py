# backend/main/main.py

from fastapi import FastAPI, HTTPException
from pony.orm import db_session
from starlette.requests import Request
from starlette.responses import JSONResponse
from app.api import auth
from db import init_db
from db.models import User

app = FastAPI()

init_db()

app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"},
    )

# Create admin user if not already present
@db_session
def create_admin():
    admin = User.get(isAdmin=True)
    if not admin:
        try:
            admin = User(
                username="admin",
                password="password",
                company="admin_company",
                email="admin@example.com",
                isAdmin=True
            )
            return "Admin user created successfully"
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

create_admin()

