from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Database connection details
DATABASE_USER = 'root'
DATABASE_PASSWORD = ''
DATABASE_HOST = 'localhost'
DATABASE_PORT = '3306'
DATABASE_NAME = 'sync'

# Construct the database URL
DATABASE_URL = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

# Create the engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for our classes definitions
Base = declarative_base()
