# RESTful Web Service with FastAPI and Pydantic

## Objective
To develop a high-performance RESTful web service using FastAPI, leveraging Pydantic for data validation and automatic interactive API documentation.

## Algorithm
1. Initialize a FastAPI application instance.
2. Define typed request schemas using Pydantic `BaseModel`.
3. Implement `GET` and `POST` routes with built-in validation and exception handling.
4. Run and test endpoints via Uvicorn and interactive Swagger documentation.

## Input
* JSON payloads containing item attributes (`name`, `description`, `price`, `tax`).

## Output
* Serialized JSON responses, validation feedback, and ASGI server execution logs.

## Time & Space Complexity
* **Time Complexity**: O(1) for direct item insertions and lookups in the memory list.
* **Space Complexity**: O(N) where $N$ is the number of stored item records in memory.
