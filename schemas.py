from pydantic import BaseModel, ConfigDict

class StudentCreate(BaseModel):
    name : str
    email : str

class StudentResponse(BaseModel):
    id : int
    name : str
    email : str


    model_config = ConfigDict(from_attributes=True) 
