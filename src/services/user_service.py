from entities.user import User
from repositories.user_repository import UserRepository


class UserService:
    def __init__(self, conn=None):
        if conn is None:
            self.user_repository = UserRepository()
        else:
            self.user_repository = UserRepository(conn)

    def login(self, username, password):
        db_password = self.user_repository.get_password(username)
        if db_password is None:
            return "No username found. Create new user."
        if db_password != password:
            return "Wrong password"
        return "Welcome"

    def create(self, username, password):

        if len(username) > 1:
            if self.user_repository.check_username_exists(username):
                return "User already exists."
            self.user_repository.create_user(User(username, password))
            return "User created."
        return "Username too short. Must contain at least 2 characters."
