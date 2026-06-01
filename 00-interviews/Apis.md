# Common Question based on API Design

## Exlain the REST Principles
REST (Representational State Transfer) isn’t a protocol but a set of architectural principles for designing networked applications—especially web APIs. It was introduced by Roy Fielding in his doctoral dissertation.

### 🔑 Core Principles of REST

#### 1. Client–Server Architecture
- The client and server are separate concerns.
    1. Client → Handles UI/UX (frontend, mobile app)
    2. Server → Handles data, logic, APIs

- Why it matters:
    1. Independent development
    2. Better scalability
    3. Easier maintenance
Example:
React app (client) calls Django API (server)

#### 2. Statelessness
- Each request from client → server must contain all the information needed.
    1. Server does NOT store client session
    2. Every request is independent

👉 Why it matters:
Easier scaling (no session management)
Better reliability

```http
GET /users/1
Authorization: Bearer <token>
```
- Every request carries auth info → server doesn’t remember previous calls.

#### 3. Cacheability
- Responses should indicate whether they are cacheable or not.
👉 Why it matters:
    1. Improves performance
    2. Reduces server load

```python
Cache-Control: max-age=3600
```
- Browser/API can reuse response for 1 hour

#### 4. Uniform Interface (MOST IMPORTANT)
It ensures consistent API design using:

1. Resource-Based URLs: Use nouns, not verbs.
```http

# Goood Examples
/users
/orders/123

# Bad Examples
/getUsers
/createOrder
```

2. Standard HTTP Methods
| Method | Meaning          |
| ------ | ---------------- |
| GET    | Retrieve data    |
| POST   | Create           |
| PUT    | Update (full)    |
| PATCH  | Update (partial) |
| DELETE | Remove           |

3. Representation: Resources are sent in formats like: JSON (most common) and XML

4. Self-descriptive Messages: Each request/response contains enough info: Headers and Status codes

#### 5. Layered System
Client doesn’t know if it’s talking to:
- Actual server
- Proxy
- Load balancer

👉 Why it matters:
- Improves scalability
- Adds security layers

## Explain how you would implement asynchronous processing in a FastAPI-based microservice and when async can actually hurt performance.

Implementing asynchronous processing in FastAPI is straightforward because the framework is built on Starlette, which is designed for high-performance asyncio operations.

### 1. Implementation Strategy
To implement async correctly, you must ensure that the entire chain of execution—from the route handler to the database driver—is non-blocking.

#### A. The Route Handler
Use the `async def` keyword. This tells FastAPI to run the function in the existing event loop rather than spawning a thread from a thread pool.

#### B. Asynchronous Clients & Drivers
If you use async def but then call a blocking library (like requests or a standard psycopg2 driver), you defeat the purpose. You must use async-native libraries:

- **HTTP Requests**: Use `httpx` or `aiohttp` instead of requests.

- **Databases:** Use `asyncpg` (PostgreSQL), `motor` (MongoDB), or SQLAlchemy with the +aiopg or +asyncpg dialect.

- **Background Tasks:** Use FastAPI's built-in BackgroundTasks for small jobs or Celery/ARQ for heavy lifting.

## A downstream service starts timing out intermittently. How would you make your microservice resilient and prevent cascading failures?