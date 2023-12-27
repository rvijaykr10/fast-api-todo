from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4

app = FastAPI()

class TodoPost(BaseModel):
    title: str

class TodoPut(BaseModel):
    id: Optional[UUID]
    title: Optional[str]
    completed: Optional[bool]
    
TODOS = []

@app.get('/')
async def get_todos():
    return TODOS

@app.get('/{id}')
async def get_todo(id):
    if len(list(filter(lambda x : str(x['id']) == id, TODOS))) == 0:
        return f'todo with id {id} not found'
    
    return list(filter(lambda x : str(x['id']) == id, TODOS))

@app.post('/')
async def add_todo(todo: TodoPost):
    new_todo = {'id': uuid4(), 'title': todo.title, 'completed': False}
    TODOS.append(new_todo)
    return new_todo

@app.put('/')
async def update_todo(todo: TodoPut):
    if len(list(filter(lambda x : str(x['id']) == id, TODOS))) == 0:
        return f'todo with id {id} not found'
    
    todo_to_update = list(filter(lambda x : x['id'] == todo.id, TODOS))[0]
    todo_index = TODOS.index(todo_to_update)
    todo_to_update['title'] = todo.title
    todo_to_update['completed'] = todo.completed
    TODOS.pop(todo_index)
    TODOS.insert(todo_index, todo_to_update)
    return todo_to_update

@app.delete('/{id}')
async def del_todo(id):
    global TODOS
    if len(list(filter(lambda x : str(x['id']) == id, TODOS))) == 0:
        return f'todo with id {id} not found'
    
    TODOS = list(filter(lambda x : str(x['id']) != id, TODOS))
    return 'Todo Deleted'