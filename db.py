from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import os

DATABASE_URL=os.environ['DATABASE_URL']

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase): pass

