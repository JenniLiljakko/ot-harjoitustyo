import unittest
from repositories.exercise_repository import ExerciseRepository
from entities.exercise import Exercise
from database import connection_test

class TestExerciseRepository(unittest.TestCase):
    def setUp(self):
        self.exercise_repository = ExerciseRepository(connection_test)
        ExerciseRepository()
        
      
