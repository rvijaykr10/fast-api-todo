from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4
import database

app = FastAPI()

class TodoPost(BaseModel):
    title: str
    completed: bool

# class TodoPut(BaseModel):
#     id: Optional[UUID]
#     title: Optional[str]
#     completed: Optional[bool]
    
# TODOS = []

database.create_table()

@app.get('/')
async def get_todos():
    todos = database.show_todos()
    return todos

# @app.get('/{id}')
# async def get_todo(id):
#     if len(list(filter(lambda x : str(x['id']) == id, TODOS))) == 0:
#         return f'todo with id {id} not found'
    
#     return list(filter(lambda x : str(x['id']) == id, TODOS))

@app.post('/')
async def add_todo(todo: TodoPost):
    database.add_todo(todo.title, todo.completed)

# @app.put('/')
# async def update_todo(todo: TodoPut):
#     if len(list(filter(lambda x : str(x['id']) == id, TODOS))) == 0:
#         return f'todo with id {id} not found'
    
#     todo_to_update = list(filter(lambda x : x['id'] == todo.id, TODOS))[0]
#     todo_index = TODOS.index(todo_to_update)
#     todo_to_update['title'] = todo.title
#     todo_to_update['completed'] = todo.completed
#     TODOS.pop(todo_index)
#     TODOS.insert(todo_index, todo_to_update)
#     return todo_to_update

# @app.delete('/{id}')
# async def del_todo(id):
#     global TODOS
#     if len(list(filter(lambda x : str(x['id']) == id, TODOS))) == 0:
#         return f'todo with id {id} not found'
    
#     TODOS = list(filter(lambda x : str(x['id']) != id, TODOS))
#     return 'Todo Deleted'