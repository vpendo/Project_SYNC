from sqlalchemy import Column, Integer, String
from database.database import Base

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, default="")  # Non-nullable for uniqueness
    full_name = Column(String(50), nullable=True, default="")
    password_hash = Column(String(255), nullable=True, default="")
