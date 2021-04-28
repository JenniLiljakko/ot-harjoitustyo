from entities.exercise import Exercise
from database import connection


class ExerciseRepository:
    def __init__(self, conn=None):
        if conn is None:
            self._connection = connection
        else:
            self._connection = conn

    def get_levels(self):
        cursor = self._connection.cursor()
        return cursor.execute("SELECT DISTINCT exercise_level FROM exercises").fetchall()

    def get_exercise_number_for_level(self, level):
        cursor = self._connection.cursor()
        return cursor.execute("SELECT exercise_number FROM exercises WHERE exercise_level = ?", (level,)).fetchall()

    def get_exercise(self, exercise_number):
        cursor = self._connection.cursor()
        return cursor.execute("SELECT exercise FROM exercises WHERE exercise_number=?", (exercise_number,)).fetchone()

    def get_answer(self, exercise_number):
        cursor = self._connection.cursor()
        return cursor.execute("SELECT answer FROM exercises WHERE exercise_number=?", (exercise_number,)).fetchone()

            