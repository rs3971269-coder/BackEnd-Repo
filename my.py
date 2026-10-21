import os
from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from pydantic import BaseModel, ConfigDict
from sqlalchemy import create_engine, String
from sqlalchemy.orm import (
    sessionmaker, DeclarativeBase, Session, Mapped, mapped_column
)

# ---- database part (already filled in) ----
load_dotenv()
DATABASE_URL = os.environ.get('DATABASE_CONNECTION_URL')
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)    


class Base(DeclarativeBase):
    pass


def get_db():
    # TODO: create a session, yield it, and always close it
    
    try:
        session = SessionLocal()
        yield session
    finally:
        session.close

# ---- models part ----
class Department(Base):
    # TODO: table name and the three columns
    __tablename__ = "department"

    id : Mapped[int] = mapped_column(
        primary_key=True
    )

    name : Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    code : Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False
    )


Base.metadata.create_all(engine)

# ---- schemas part ----
class DepartmentCreate(BaseModel):
    # TODO: request fields
    name : str
    code : str

class DepartmentResponse(BaseModel):
    # TODO: allow reading from ORM attributes, then the response fields
    id : int
    name : str
    code : str
# TODO: create the tables (think about where this line must go)
    model_config = ConfigDict(from_attributes=True)


app = FastAPI(title="Student Management API")

# TODO: write the POST /departments route

@app.post('/departments', response_model=DepartmentResponse)
def Create_department(department_data: DepartmentCreate, session : Session = Depends(get_db)):
    department = Department(
        name = department_data.name,
        code = department_data.code
    )

    session.add(department)
    session.commit()
    session.refresh(department)

    return department