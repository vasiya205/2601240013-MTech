# Database-Backed Web Service using SQLAlchemy ORM and FastAPI

## Objective
To develop a persistent RESTful web service using FastAPI combined with SQLAlchemy ORM and SQLite database connectivity.

## Algorithm
1. Configure SQLAlchemy engine, session maker, and declarative base.
2. Define relational database models for entities.
3. Establish FastAPI dependency injection for session handling.
4. Implement CRUD endpoints backed by persistent storage.

## Input
* Product JSON entries containing attributes (`name` and `price`).

## Output
* Stored database records, serialized JSON API responses, and server logs.

## Time & Space Complexity
* **Time Complexity**: O(N) for querying collections from the database.
* **Space Complexity**: O(D) where $D$ represents disk storage utilized by the SQLite database file.
