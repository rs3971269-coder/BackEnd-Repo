# from fastapi import FastAPI
# from pydantic import BaseModel 

# app = FastAPI()

# def authenticatte_token(token : str):
#     if token == None:
#         return -1
#     elif token == 'ABC':
#         return 3
#     elif token == 'PQR':
#         return 2
#     elif token == 'MNO':
#         return 1
#     else:
#         return -1

# order_data = {
#     1:[13,25],
#     2:[32],
#     3:[23,26]
# }

# class LoginRequest(BaseModel):
#     username : str
#     password : str

# user_password_data = {
#     'Tanshik' : 'ABCDEFG',
#     'Aman' : 'PQRST',
#     'Yaman' : 'ABCER'
# }

# tokens = {
#     'Tanshik' : 'ABC',
#     'Aman' : 'PQR',
#     "Yaman" : 'MNO'
# }

# @app.post("/login")
# def login(login_request: LoginRequest):
#     if user_password_data.get(login_request.username) == login_request.password:
#         return tokens.get(login_request.username, "")
#     return ""


# @app.get('/profile')
# def profile():
#     return {'message' : 'profile API'}

# @app.get('/orders')
# def order(token : str):
#     user_id = authenticatte_token(token)
#     if user_id == None:
#         return{'error' : 'Please check you id that not match to data'}
#     return order_data[user_id]
    

# @app.get('/payments')
# def payment():
#     return []




# from fastapi import FastAPI, Depends

# app = FastAPI()


# token = {"T1": 101, "T2": 102}

# courses_data = {
#     101: ["CS101", "CS202"],
#     102: ["MATH101"],
# }

# certificates_data = {
#     101: ["CERT-CS101"],
#     102: [],
# }

# AUTH_ERROR = {"error": "User is not authenticated, please pass correct token"}

# def authenticate_token(token: str):
#     # TODO: look up token in TOKEN_TO_USER, return -1 if not found
   
#     if token == 'T1':
#         return 101
#     elif token == 'T2':
#         return 102
#     else:
#         return -1
    


# # TODO: call authenticate_token and return its result
# def get_current_user(token: str):
#     return authenticate_token(token)

# @app.get("/courses")
# def courses(user_id: int = Depends(get_current_user)):
#     # TODO: return the course list for user_id, or AUTH_ERROR if user_id == -1
#     if user_id == -1:
#         return AUTH_ERROR
#     return courses_data.get(user_id,[])

# @app.get("/certificates")
# def certificates(user_id: int = Depends(get_current_user)):
#     # TODO: return the certificate list for user_id, or AUTH_ERROR if user_id == -1
#     if user_id == -1:
#         return AUTH_ERROR
#     return certificates_data.get(user_id,[])


from fastapi import FastAPI,Depends,Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi import BackgroundTasks, UploadFile,File

app = FastAPI()


# app.add_middleware(
#     CORSMiddleware,
#     allow_origin = ['http://127.0.0.1:5500'],
#     allow_credentials = True,
#     allow_methods = ["*"] #allow all type of api request from http://127.0.0.1:5500/
# )

# @app.get('/Users')
# def get_user():
#     return ['user1','user2','user3']


class SendEmail(BaseModel):
    emailText : str

def send_email(email):
    print('Sending Email' , email)

@app.post('/send-email')
def sendEmail(emailbody : SendEmail, background_tasks : BackgroundTasks):
    # send_email(emailbody.emailtext) #10
    background_tasks.add_task(send_email,emailbody.emailText) #only milli seconds
    return {'message':'Email has benn schulded successfully'}   


@app.post('/upload')
async def upload_file(file : UploadFile = File(...)):
    content = await file.read()
    with open(f"upload/{file.filename}","wb") as f:
        f.write(content)
    return {
        "fileName" : file.filename,
        "content_type" : file.content_type
    }

@app.get('/download{filename}')
def download_file(filename : str):
    file_path = f"upload/{filename}"

    return FileResponse (
        path = file_path,
        filename = filename 
    )
