import unittest
from services.user_service import UserService
from repositories.user_repository import UserRepository
from entities.user import User
from database import connection_test

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.service = UserService(connection_test)
        UserService()
        self.user_repository = UserRepository(connection_test)
        self.user_repository.delete_all()
        self.user_maija = User('maija', 'maijanen')
        self.user_repository.create_user(self.user_maija)

    def test_login(self):
        self.assertEqual(self.service.login('maija', 'maijanen'), "Welcome")
        self.assertEqual(self.service.login('maija', 'wrong'), "Wrong password")
        self.assertEqual(self.service.login('laura', 'mikkonen'), \
                                "No username found. Create new user.")

    def test_create(self):
        self.assertEqual(self.service.create('maija', 'maijanen'), "User already exists.")
        self.assertEqual(self.service.create('mikko', 'mikkonen'), "User created.")
        self.assertEqual(self.service.create('m', '123'), \
                            "Username too short. Must contain at least 2 characters.")
