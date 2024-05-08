from fastapi import Depends
from pony.orm import db_session, commit
from app.database.models import User
from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException
import secrets
from app.security import oauth2_scheme

import logging

logger = logging.getLogger(__name__)


# Creating a passlib context for hashing passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Generate a strong, randomly generated secret key for JWT token
SECRET_KEY = secrets.token_urlsafe(32)

# Algorithm for JWT token
ALGORITHM = "HS256"

# Token expiration time (e.g., 30 minutes)
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# Function to verify the password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Function to authenticate user
def authenticate_user(username: str, password: str):
    user = User.get(username=username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

# Function to create JWT token
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Function to decode JWT token
def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Signature has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

@db_session
def create_user(username: str, password: str, company: str, email: str):
    existing_user = User.get(email=email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    # Hash the password
    hashed_password = pwd_context.hash(password)

    # Create the user with is_admin set to False
    user = User(
        username=username,
        password=hashed_password,
        company=company,
        email=email,
        is_admin=False
    )

# Function to check if user is admin
def is_admin(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    if not payload.get("is_admin"):
        raise HTTPException(status_code=403, detail="User does not have admin privileges")


@db_session
def delete_user(user_id: int):
    user = User.get(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.delete()
    commit()  # Commit the transaction after deletion






