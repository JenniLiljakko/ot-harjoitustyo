from entities.user import User
from database import connection


class UserRepository:
    def __init__(self):
        self._connection = connection

    def create_user(self, user):
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user.username, user.password))
        self._connection.commit()

    def get_password(self, username):
        cursor = self._connection.cursor()
        password = cursor.execute("SELECT password FROM users WHERE username=?", (username,)).fetchone()
        if password is None:
            return None
        else:
            return password[0]

    def check_username_exists(self, username):
        cursor = self._connection.cursor()
        username = cursor.execute("SELECT username FROM users WHERE username=?", (username,)).fetchone()
        if username is None:
            return False
        else:
            return True

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM users')
        self._connection.commit()

    def count_users(self):
        cursor = self._connection.cursor()
        count = cursor.execute('SELECT COUNT(*) FROM users').fetchone()
        return count[0]
