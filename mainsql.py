from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, session, sessionmaker
from sqlalchemy import String, create_engine, select
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.environ['DATABASE_CONNECTION_URL']
engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__='Student'

    id : Mapped[int] = mapped_column(
        primary_key=True
    )

    name : Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    email : Mapped[str] = mapped_column(
        String(250),
        unique=True,
        nullable=False
    )

    address : Mapped[str] = mapped_column(
        String(400),
        nullable=False
    )

session = sessionLocal()

try:
    #INSERT DATA IN TABLE
    # student = Student(id=1,
    #                 name="Rohit Sharma", 
    #                 email="main@example.com",
    #                 address="Delhi")
    
    # session.add(student)
    # session.commit()

    #SELECT THE FROM TABLE

    #1 RETURN -> A list of objects
    stmt = select(Student)
    student = session.scalars(stmt).all() 
    for s in student:
        # print(student) this give an object not readabble for people like ->[<__main__.Student object at 0x0000025446617F50>, <__main__.Student object at 0x0000025446617FD0>, <__main__.Student object at 0x0000025446638110>]
        print(f' id : {s.id}, Name : {s.name}, Email : {s.email}, Address : {s.address}')

    #2 RETURN -> The object, or None
    student = session.get(Student, 1)
    if student is not None:
        print(student.name)
    else:
        print("Student not found with ID 1")

    #3 RETURN -> A list of matching objects
    stmth = select(Student).where(Student.id > 1)
    students = session.scalars(stmth).all()
    for s in students:
        print(s.name)


    #UPDATE AND DELETE -  Both follow the same rhythm: fetch the object, act on it, then commit.
    student = session.get(Student,1)
    student.email = "changeemail@dummy.com"
    session.commit()

    student = session.get(Student, 1)
    session.delete(student)
    session.commit()

# Tables are created through the engine.
# Queries run only through the session.
# Every change reaches the database only on commit().
    
finally:
    session.close()

Base.metadata.create_all(engine)

