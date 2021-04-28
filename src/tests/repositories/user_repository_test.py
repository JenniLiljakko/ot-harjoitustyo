import unittest
from repositories.user_repository import UserRepository
from entities.user import User
from database import connection_test

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.user_repository = UserRepository(connection_test)
        UserRepository()
        self.user_repository.delete_all()
        self.user_maija = User('maija', 'maijanen')
        self.user_minna = User('minna', 'minnala')

    def test_create_user(self):
        initial_count = self.user_repository.count_users()
        self.user_repository.create_user(self.user_maija)
        final_count = self.user_repository.count_users()
        self.assertTrue(self.user_repository.check_username_exists('maija'))
        self.assertEqual(initial_count+1, final_count)

    def test_get_password(self):
        self.user_repository.create_user(self.user_maija)
        password = self.user_repository.get_password('maija')
        self.assertEqual(password, 'maijanen')
        password_2 = self.user_repository.get_password('laura')
        self.assertEqual(password_2, None)

    def test_check_username_exists(self):
        self.user_repository.create_user(self.user_minna)
        self.assertTrue(self.user_repository.check_username_exists('minna'))
        self.assertFalse(self.user_repository.check_username_exists('minno'))