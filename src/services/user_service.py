from entities.user import User
from repositories.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()


    def login(self, username, password):
        
        db_password = self.user_repository.get_password(username)
        if db_password is None:
            return "No username found. Create new user."
        else:
            if db_password != password:
                return "Wrong password"
            else:
                return "Welcome"
    
    def create(self, username, password):

        if len(username) > 1:
            if self.user_repository.check_username_exists(username):
                return "User already exists."
            else:
                self.user_repository.create_user(User(username,password))
                return "User created."
        else:
            return "Username too short. Must contain at least 2 characters."