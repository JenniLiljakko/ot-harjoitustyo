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
            create table excercises (
                excercise text,
                excercise_number integer primary key,
                subject text,
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


def start():
    drop_tables()
    create_tables()

