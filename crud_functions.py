import sqlite3
import random

connection = sqlite3.connect(".venv/database_module14.db")
cursor = connection.cursor()

def initiate_db():

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL 
    )
    ''')

    cursor.execute("DELETE FROM Products")

    for i in range(1, 5):
        cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                           (f"Продукт {i}", f"Описание {i}", f"{i * 100}"))

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL 
        )
        ''')

    cursor.execute("DELETE FROM Users")
    connection.commit()

def get_all_products():
    cursor.execute("SELECT * FROM Products")
    db = cursor.fetchall()
    connection.commit()
    return list(db)

def add_user(username, email, age):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"Пользователь {username}", f"{email}", f"{age}", "1000"))
    connection.commit()

def is_included(username):
    if cursor.execute(f"SELECT COUNT(*) FROM Users WHERE username = '{username}'").fetchone():
        return True
    else:
        return False

initiate_db()