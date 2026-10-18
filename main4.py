from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from schemas import StudentCreate, StudentResponse
from model import Student
from database import get_db, Base, engine
from fastapi import HTTPException

Base.metadata.create_all(bind=engine)

app = FastAPI(title='Student Management API')

@app.post('/student', response_model=StudentResponse)
def create_student(student_data: StudentCreate, db: Session = Depends(get_db)):
    student = Student(
        name=student_data.name,
        email=student_data.email
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    return student


@app.get('/student', response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()

@app.get('/student/{student_id}', response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.get(Student, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student