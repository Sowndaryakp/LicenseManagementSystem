from fastapi import FastAPI, HTTPException
from app.database import init_database

from fastapi.middleware.cors import CORSMiddleware

from app.routers import user_router
from pony.orm import db_session
from app.database.models import User
from passlib.context import CryptContext

app = FastAPI()

# DB_URL = "postgres://postgres:password@localhost:5432/postgres"
init_database()

app.include_router(user_router)

# Creating a passlib context for hashing passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# CORS (Cross-Origin Resource Sharing) Configuration
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://yourdomain.com",
    "https://yourdomain.com"
]

# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create admin user if not already present
@db_session
def create_admin():
    admin = User.get(is_admin=True)
    if not admin:
        try:
            hashed_password = pwd_context.hash("password")  # Hash the default password
            admin = User(
                username="admin",
                password=hashed_password,
                company="admin_company",
                email="admin@example.com",
                is_admin=True
            )
            return "Admin user created successfully"
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

create_admin()


# to RUN
# uvicorn main:app --reload --host 172.18.101.47 --port 6699
