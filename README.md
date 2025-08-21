![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Ready-brightgreen)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)

# FastAPI + MySQL + Docker 
This project demonstrates the a production ready backend API built with **FastAPI** , **MySQL**, and **Docker**.
It includes databases models, CRUD Operations and containerized deployment using `docker-compose`.

## Features
- FastAPI for building REST APIs
- MySQL database with SQLALCHEMY ORM
- CRUD Operations
- Dockerized for easy Deployment

## 📂 Project Structure
- app/ → API source code
  -  main.py  → Entry point (Endpoints)
  -  database.py → Database Connection & Session
  -  models.py → SQLALCHEMY Models
  -  schema.py→ Pydantic Schemas
- Dockerfile → Build Intructions for Fastapi image

- docker-compose.yml → Multi-container setup

- requirements.txt → Dependencies


#  API Endpoints

- `POST /users/` → Create user  
- `GET /users/` → Get all user  
- `GET /users/{id}` → Get user by ID  
- `PUT /users/{id}` → Update user
- `DELETE /users/{id}` → Delete user
