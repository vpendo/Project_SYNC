from pydantic import BaseModel, EmailStr, constr

class UserCreate(BaseModel):
    email: EmailStr
    full_name: constr(max_length=50) = None
    password_hash: constr(max_length=255) = None

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: constr(max_length=255) = None

