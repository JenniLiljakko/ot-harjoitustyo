import unittest
from services.exercise_service import ExerciseService
from database import connection_test

class TestExerciseService(unittest.TestCase):
    def setUp(self):
        self.service = ExerciseService(connection_test)
        ExerciseService()

    def test_get_levels_list(self):
        levels = self.service.get_levels_list()
        self.assertTrue(1 in levels)
        self.assertTrue(2 in levels)
        self.assertTrue(3 in levels)

    def test_get_exercise_number_list(self):
        numbers = self.service.get_exercise_number_list(1)
        self.assertTrue(1 in numbers)
        self.assertTrue(2 in numbers)
        self.assertTrue(3 in numbers)

    def test_get_exercise_text(self):
        exercise = self.service.get_exercise_text(1)
        self.assertEqual(exercise, '2*1')

    def test_check_answer(self):
        self.assertEqual(self.service.check_answer(3, 1), "incorrect :(")
        self.assertEqual(self.service.check_answer(2, 1), "correct! :)")
