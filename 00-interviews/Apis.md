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
