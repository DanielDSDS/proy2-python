from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""
    Se crea una sesión para la base de datos y 
  se define una función para acceder desde los demas modulos 
"""

DB_URL = "sqlite:///./chinook.db" 
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})

local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()
