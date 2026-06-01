# The Core Idea
In FastAPI, a route is a combination of an HTTP method + a URL path + a Python function. FastAPI uses Python decorators to bind them together, and it automatically handles request parsing, validation, and response serialization via Pydantic.

## 1. Basic Routes
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, world"}

@app.post("/items")
def create_item():
    return {"status": "created"}
```
- FastAPI supports all standard HTTP methods: `get`, `post`, `put`, `patch`, `delete`, `head`, `options`, `trace`.

## 2. Path Parameters
- Capture dynamic segments from the URL using {param} syntax:

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):   # auto-validated as int
    return {"user_id": user_id}

@app.get("/files/{file_path:path}")   # :path matches slashes too
def get_file(file_path: str):
    return {"path": file_path}
```

- The type annotation (`int`, `str`, `UUID`, etc.) triggers automatic validation and coercion. A non-integer `user_id` returns a `422` Unprocessable Entity without any extra code.

## 3. Query Parameters
- Any function parameter that isn't in the path is treated as a query param:

```python
@app.get("/items")
def list_items(skip: int = 0, limit: int = 10, search: str | None = None):
    return {"skip": skip, "limit": limit, "search": search}
```
- **GET** `/items?skip=20&limit=5&search=book` → parsed, typed, and validated automatically. Optional params use None as default.

