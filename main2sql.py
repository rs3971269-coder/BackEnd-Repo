from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, session, sessionmaker, relationship
from sqlalchemy import String, ForeignKey, create_engine
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.environ['DATABASE_CONNECTION_URL']
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass

class Department(Base):
    __tablename__ = "departments"
    id : Mapped[int] = mapped_column(
        primary_key=True
    )
    name : Mapped[str] = mapped_column(
        String(100),
        nullable=False  
    )

class Employess(Base):
    __tablename__ = "employess"
    id : Mapped[int] = mapped_column(
        primary_key=True
    )
    name : Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )
    department_id: Mapped[int] = mapped_column(
        ForeignKey("departments.id"),
        nullable=False
    )
    
    department : Mapped["Department"] = relationship()


Base.metadata.create_all(engine)



session = SessionLocal()
try:
    cs_department = Department(id=1, name="Computer Science")
    rahul = Employess(id=1, name="Rahul", department=cs_department)
    aman = Employess(id=2, name="Aman", department=cs_department)
    session.add_all([cs_department, rahul, aman])
    session.commit()
finally:
    session.close()

