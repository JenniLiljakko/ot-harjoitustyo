import sqlite3
import os

dirname = os.path.dirname(os.path.abspath(__file__))
database_filepath = os.path.join(dirname, '../data/database.sqlite')

connection = sqlite3.connect(database_filepath)
connection.row_factory = sqlite3.Row
connection.isolation_level = None



def create_tables():
    cursor = connection.cursor()

    cursor.execute('''
            create table users (
                username text primary key,
                password text
            );
    ''')

    cursor.execute('''
            create table exercises (
                exercise_number integer primary key,
                exercise_level integer,
                exercise text,
                answer real
            );
    ''')

    connection.commit()


def drop_tables():
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')
    cursor.execute('''
        drop table if exists excercises;
    ''')

    connection.commit()

def add_exercises():
    cursor = connection.cursor()
    for i in range(1,11):
        if i<4:
            level=1
        elif i>=4 and i<7:
            level=2
        else:
            level=3
        cursor.execute('INSERT INTO exercises (exercise_number, exercise_level, exercise, answer) VALUES ({},{}, \'{}\', {}); '.format(i, level, '2^{}'.format(i),2**i))

def start():
    drop_tables()
    create_tables()
    add_exercises()

