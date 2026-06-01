"""
===================================================================================================
In my world, a route consists of three main parts: the decorator, the path, and the operation function.

1. Operation: Refers to the HTTP method (GET, POST, PUT, DELETE, etc.).

2. Path: The endpoint URL.

3. Function: The code that runs when someone hits that path.
===================================================================================================
"""


from fastapi import FastAPI

# The app instance
app = FastAPI(debug=True)

# Basic Route
@app.get('/')
async def home_page():
    resp = {"message": "Hello World"}
    return resp


# Route with params
@app.get("/users/{user_id}")
async def get_user_id(user_id: int):
    id = user_id
    resp = {"message": f"Found the request for user id:{id}"}
    return resp

@app.get('/files/{file_path: path}')
def get_filepath(file_path: str):

    return file_path