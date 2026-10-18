import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

load_dotenv()

DATABASE_URL = os.environ['DATABASE_CONNECTION_URL']
engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    session = sessionLocal()
    try:
        yield session 
    finally:
        session.close()

#yield session hands the session to whoever called it (for example, your API route) and pauses the function.
# When the caller is finished, execution resumes after the yield.