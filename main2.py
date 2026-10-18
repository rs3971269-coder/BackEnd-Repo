from fastapi import FastAPI, Query # query for validation of order ,like greaterthan , smallthan etc,
from pydantic import BaseModel

app = FastAPI()


# #Dynamic route 
# @app.get("/students/{student_id}")
# def get_student(student_id: int):
#     return {
#         "student_id": student_id,
#     }

##Dynamic route with query parameter
# @app.get("/students/{student_id}")
# def get_student(student_id: int, email : str = None, doj : int = None, Address = "Delhi"):
#     return {
#         "student_id": student_id,
#         "email" : email,
#         "doj" : doj,
#         "Address" : None
#     }

# #different API 
# @app.get("/students/{student_id}/hello")
# def get_student_hello(student_id:int = None):
#     return {"message": f"hello, student {student_id}!"}


@app.get("/students/{student_id}")
def get_student(student_id : int, age : int = Query(gt=0, lt=100)):
    return{
        "student_id" : student_id,
        "age" : age
    }

@app.get("/students/{student_id}")
def get_student(student_id : int, Name : str = Query(min_length=12,max_langth=20)):
    return{
        "student_id" : student_id,
        "Name" : Name
    }




# a Pydantic request model and response model for a feedback API so an internal score field never reaches the client.
# Post api deepdive about response_model, response_model - this model use for response validation, and also for documentation purpose, it will not show password in the response model.

#pydantic request model
class Student(BaseModel):
    name : str
    age : int
    email : str
    password : str

#pydantic response model
class StudentCreateResponse(BaseModel):
    name : str
    age : int
    email : str

@app.post("/students", response_model=StudentCreateResponse)
def create_student(new_student : Student):
    print(new_student.age)
    return {
        "name" : new_student.name,
        "age" : new_student.age,
        "email" : new_student.email,
        "password" : new_student.password
    }


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class FeedbackRequest(BaseModel):
    user_name : str
    course_id : int
    comment : str

class FeedbackResponse(BaseModel):
    user_name : str
    course_id : int
    comment : str
    
@app.post("/feedback", response_model=FeedbackResponse)  # TODO: attach the response_model here
def submit_feedback(data: FeedbackRequest):
    moderation_score = 0.92  # internal-only value, never send this to the client
    result = {
        "user_name": data.user_name,
        "course_id": data.course_id,
        "comment": data.comment,
        "moderation_score": moderation_score,
    }
    return result

## hardcoded TOKEN in autotication in  this sesson 


