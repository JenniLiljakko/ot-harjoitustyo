import unittest
from repositories.exercise_repository import ExerciseRepository
from entities.exercise import Exercise
from database import connection_test

class TestExerciseRepository(unittest.TestCase):
    def setUp(self):
        self.exercise_repository = ExerciseRepository(connection_test)
        ExerciseRepository()
        self.exercise = Exercise(1, 1, '2*1', 2)

    def test_get_levels(self):
        levels = self.exercise_repository.get_levels()
        levels = [level[0] for level in levels]
        self.assertTrue(1 in levels)
        self.assertTrue(2 in levels)
        self.assertTrue(3 in levels)

    def test_get_exercise_number_for_level(self):
        exc_numbers = self.exercise_repository.get_exercise_number_for_level(1)
        exc_numbers = [exc[0] for exc in exc_numbers]
        self.assertTrue(1 in exc_numbers)
        self.assertTrue(2 in exc_numbers)
        self.assertTrue(3 in exc_numbers)

    def test_get_exercise(self):
        exercise = self.exercise_repository.get_exercise(self.exercise.exercise_number)[0]
        self.assertEqual(exercise, self.exercise.exercise)

    def test_get_answer(self):
        answer = self.exercise_repository.get_answer(self.exercise.exercise_number)[0]
        self.assertEqual(answer, self.exercise.answer)
