import sqlite3
from pprint import pprint
with sqlite3.connect('test.db') as connection:
    cursor = connection.cursor()
def crate_table_user(cursor):
    command = """
         CRATE TABLE IF NOT EXISTS users (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         surname TEXT NOT NULL,
         gender TEXT NOT NULL
    )"""
    cursor.execute(command)
class user:
    def __init__(self, name, surname, gender):
        self.name=name
        self.surname=surname
        self.gender=gender
    def __str__(self):
        return f'{self.name} {self.surname} {self.gender}'
def add_user(cursor, profile):
    command = """
        INSER INTO users (name, surname, gender)
        VALUES (?, ?, ?)
        """
    cursor.execute(command,(profile.name, profile.surname, profile.gender))
def get_users_list(cursor, id):
    command="""
         SELECT * FROM users
         WHERE id = ?
         """
    result = cursor.execute(command, (id,))
    users = result.fetchall()
    pprint(users)
if __name__ == '__main__':
    names_list=['Иван', 'Пётр', 'Сергей', 'Екатерина', 'Владислав']
    surnames_list = ['Иванов', 'Петров', 'Сергеев', 'Катеринина', 'Прокофьев']
    genders_list = ['male','male','male', 'female', 'male']
    users_list = [user(name, surname, gender) for name, surname, gender in zip(names_list, surnames_list, genders_list)]
    with sqlite3.connect('test.db')as connection:
        cursor=connection.cursor()
        crate_table_user(cursor)
        for i in users_list:
            add_user(cursor, i)
        get_users_list(cursor)

def delete_user_by_id(cursor, id):
    command = """
        DELETE FROM users WHERE id=?
        """
    result=cursor.execute(command,(id,))

def get_user_by_gender(cursor, gender):
    command = """
    SELECT * FROM users
    WHERE gender = ?
    """
    result = cursor.execute(command, (gender,))
    users = result.fetchall()
    pprint(users)