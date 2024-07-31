from enum import Enum
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from apis import user
from fastapi import Depends
from sqlalchemy.orm import Session
from database.database import engine, SessionLocal, Base  # Adjusted import
from typing import Annotated

# Ensure all tables are created
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Api Documentation",  # Replace with your desired title
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to the specific origins you want to allow
    allow_credentials=True,
    allow_methods=["*"],  # Adjust this to the specific methods you want to allow (e.g., ["GET", "POST"])
    allow_headers=["*"],  # Adjust this to the specific headers you want to allow (e.g., ["Content-Type", "Authorization"])
)

# Include the routers from auth, apis, and otp

app.include_router(user.router)
