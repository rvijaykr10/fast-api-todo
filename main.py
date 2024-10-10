from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
# from typing import Optional
# from uuid import UUID, uuid4
import database

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TodoPost(BaseModel):
    title: str
    completed: bool

class TodoPut(BaseModel):
    id: int
    title: str
    completed: bool

database.create_table()

@app.get('/')
async def get_todos():
    todos = database.show_todos()
    return todos

@app.get('/{id}')
async def get_todo(id:int):
    # count = database.get_todo_count(id)
    # if count == 0:
    #     return f"{id} doesn't exist."
    todo = database.show_todo(id)
    return todo

@app.post('/')
async def add_todo(todo: TodoPost):
    database.add_todo(todo.title, todo.completed)
    return 'Todo Added'

@app.put('/')
async def update_todo(todo: TodoPut):
    count = database.get_todo_count(todo.id)
    if count == 0:
        return "Invalid payload."
    database.update_todo(todo.id, todo.title, todo.completed)
    return 'Todo Updated'

@app.delete('/{id}')
async def del_todo(id:int):
    count = database.get_todo_count(id)
    if count == 0:
        return "Invalid payload."
    database.delete_todo(id)
    return 'Todo Deleted'