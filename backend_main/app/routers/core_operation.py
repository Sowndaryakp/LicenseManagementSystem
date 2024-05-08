from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime, timedelta
from app.security import oauth2_scheme,OAuth2PasswordRequestForm
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ..database.crud_operation import create_user, delete_user, is_admin, authenticate_user, create_access_token, decode_access_token

router = APIRouter(prefix="/SMW", tags=["Machine monitoring"])

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/SMW/login")

@router.post("/users/")
async def create_new_user(username: str, password: str, company: str, email: str):
    try:
        create_user(username, password, company, email)
        return {"message": "User created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/login", response_model=dict)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    # Set token expiration time
    access_token_expires = timedelta(minutes=30)
    # Generate JWT token
    access_token = create_access_token(
        data={"sub": user.username, "is_admin": user.is_admin},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer", "is_admin": user.is_admin, "message": "Login successful"}

@router.delete("/users/{user_id}")
async def remove_user(user_id: int, token: str = Depends(is_admin)):
    try:
        delete_user(user_id)
        return {"message": "User deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
