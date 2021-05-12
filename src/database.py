import sqlite3
import os

dirname = os.path.dirname(os.path.abspath(__file__))
database_filepath = os.path.join(dirname, '../data/database.sqlite')

connection = sqlite3.connect(database_filepath)
connection.row_factory = sqlite3.Row
connection.isolation_level = None

test_database_filepath = os.path.join(dirname, '../data/test.sqlite')

connection_test = sqlite3.connect(test_database_filepath)
connection_test.row_factory = sqlite3.Row
connection_test.isolation_level = None



def create_tables(conn):
    cursor = conn.cursor()

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

    conn.commit()


def drop_tables(conn):
    cursor = conn.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')
    cursor.execute('''
        drop table if exists exercises;
    ''')

    conn.commit()

def add_exercises(conn):
    cursor = conn.cursor()
    for i in range(1, 11):
        if i < 4:
            level = 1
        elif i >= 7:
            level = 3
        else:
            level = 2
        cursor.execute('INSERT INTO exercises (exercise_number, exercise_level, exercise, answer) \
                         VALUES ({},{}, \'{}\', {}); '.format(i, level, '2^{}'.format(i), 2**i))

def add_test_exercises(conn):
    cursor = conn.cursor()
    for i in range(1, 11):
        if i < 4:
            level = 1
        elif i >= 7:
            level = 3
        else:
            level = 2
        cursor.execute('INSERT INTO exercises (exercise_number, exercise_level, exercise, answer) \
                        VALUES ({},{}, \'{}\', {}); '.format(i, level, '2*{}'.format(i), 2*i))


def start():
    drop_tables(connection)
    create_tables(connection)
    add_exercises(connection)

def start_test():
    drop_tables(connection_test)
    create_tables(connection_test)
    add_test_exercises(connection_test)
