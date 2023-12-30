import os
import psycopg2
# from psycopg2.extras import DictCursor
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

CREATE_TODOS_TABLE = """CREATE TABLE IF NOT EXISTS todos (
    id SERIAL PRIMARY KEY,
    title TEXT,
    completed BOOLEAN
);"""

SHOW_TODO = "SELECT * FROM todos WHERE id = %s;"
SHOW_TODOS = "SELECT * FROM todos;"
INSERT_TODO = "INSERT INTO todos (title, completed) VALUES (%s, %s);"
UPDATE_TODO = "UPDATE todos SET title=%s, completed=%s WHERE id = %s;"
DELETE_TODO = "DELETE from todos WHERE id = %s;"

connection = psycopg2.connect(os.environ.get("DATABASE_URL"))

def create_table():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_TODOS_TABLE)
            
def show_todo(id):
    with connection:
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(SHOW_TODO, (id,))
            return cursor.fetchall()
        
def show_todos():
    with connection:
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(SHOW_TODOS)
            todos = cursor.fetchall()
            return todos  # Returns a list of dictionaries

# If you need the result as a JSON string
# result = show_todos()
# json_result = json.dumps(result)
# print(json_result
            
def add_todo(title, completed=False):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_TODO, (title, completed))

def update_todo(id, title, completed):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(UPDATE_TODO, (title, completed, id))

def delete_todo(id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(DELETE_TODO, (id,))