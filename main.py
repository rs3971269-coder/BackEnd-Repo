

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "Welcome to the FastAPI application !"}

# @app.get("/Users")
# def get_users():
#     return {"users": ["Alice", "Bob", "Charlie"]}   


tasks = [
    {
        "id": 1,
        "title": "Task 1",
        "completed": False
    },
    {
        "id": 2,
        "title": "Learn all types of FastAPI",
        "completed": False
    }
]

@app.get("/tasks")
def get_tasks(task_id : int | None = None):
    if task_id == None:
        return tasks
    else:
        for task in tasks:
            if task["id"]==task_id:
                return task
        return {"error": "Task not found"}



    
# @app.get("/tasks/{task_id}")
# def get_task(task_id : int):
#     for task in tasks:
#         if task["id"]==task_id:
#             return {
#                 "title": task["title"],
#                 "completed": task["completed"]
#             }
#     return {"error": "Task not found"}





class TaskCreate(BaseModel):
    title : str

@app.post("/tasks")
def create_task(task: TaskCreate):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "completed": False
    }
    tasks.append(new_task)
    return {"message": "Task created", "task_id": new_task["id"]} 



class taskUpdate(BaseModel):
    title : str | None = None
    completed : bool | None = None


@app.put("/tasks/{task_id}")
def update_task(task_id : int, utask: taskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            if utask.title is not None:
                task["title"] = utask.title
            if utask.completed is not None:
                task["completed"] = utask.completed
            return {"message": "Task updated", "task": task}    
    return {"error": "Task not found"}



@app.delete("/tasks/{task_id}")
def delete_task(task_id : int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}
    return {"error": "Task not found"}


#Assesment 1: Create a FastAPI application with the following endpoints:
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/books")
# def get_book():
# 	return { "message" : "book catalog retrived"}



# @app.get("/")
# def get_home():
# 	return {"message":"bookstore home API"}

# @app.get("/tasks/{task_id}")
# def get_task(task_id : int):
#     return {
#         "message" : f"Task ID: {task_id}",
#         "task_id": task_id
#     }


# @app.get("/tasks/{task_id}")
# def get_task(priority: Literal["low", "medium", "high"] | None = None):
#     return {
#         "message" : f"Task ID: {task_id}",
#         "task_id": task_id
#     }


from fastapi import FastAPI, Query

app = FastAPI()

books = [
    {"id": 1, "title": "Clean Code", "price": 35},
    {"id": 2, "title": "The Pragmatic Programmer", "price": 40},
    {"id": 3, "title": "Deep Work", "price": 25},
]

@app.get("/books/{book_id}")
def get_book(book_id: int, rating: int = Query(default=None, gt=0, lt=6)):
    for book in books:
        if book["id"] == book_id:
            return {
                "id": book["id"],
                "title": book["title"],
                "price": book["price"],
                "rating": rating
            }
    return {"error": "Book not found"}


