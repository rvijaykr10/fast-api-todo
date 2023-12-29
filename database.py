import os
import psycopg2
# from psycopg2.extras import DictCursor
from dotenv import load_dotenv

load_dotenv()

CREATE_TODOS_TABLE = """CREATE TABLE IF NOT EXISTS todos (
    id SERIAL PRIMARY KEY,
    title TEXT,
    completed BOOLEAN
);"""

SHOW_TODO = "SELECT * FROM todos WHERE id = %s"
SHOW_TODOS = "SELECT * FROM todos"
INSERT_TODO = "INSERT INTO todos (title, completed) VALUES (%s, %s)"

connection = psycopg2.connect(os.environ.get("DATABASE_URL"))

def create_table():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_TODOS_TABLE)
            
def show_todo(id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SHOW_TODO, (id,))
            return cursor.fetchall()
        
def show_todos():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SHOW_TODOS)
            return cursor.fetchall()
            
def add_todo(title, completed=False):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_TODO, (title, completed))
