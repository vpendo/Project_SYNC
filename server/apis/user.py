# apis/user.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
from database.connection import db_dependency
from Tables.DatabaseTables import Users  # Ensure this import is correct
from validations.schemas import UserCreate,UserLogin

router = APIRouter(prefix="/user", tags=["Management"])

@router.post(
    "/register",
    response_model=UserCreate,
    status_code=status.HTTP_201_CREATED,
    description="Register a new user"
)
async def register_user(user: UserCreate, db: db_dependency):
    db_user = db.query(Users).filter(Users.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    db_user = Users(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login")
def Login_user(db: db_dependency,details:UserLogin):
    if not details.email and not details.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Please provide email and password")
    user_info = db.query(Users).filter(Users.email == details.email, Users.password_hash == details.password).first()
    if not user_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Account Found With Given Creditials ")
    return user_info

@router.post("/logout")
def logout_user(details: UserLogin, db: Session = Depends(db_dependency)):
    
    return {"message": "User logged out successfully"}