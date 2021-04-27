from entities.exercise import Exercise
from repositories.exercise_repository import ExerciseRepository


class ExerciseService:
    def __init__(self):
        self.exercise_repository = ExerciseRepository()

    def get_levels_list(self):
        levels = self.exercise_repository.get_levels()
        db_levels = [level[0] for level in levels]
        return db_levels

    def get_exercise_number_list(self, level):
        exercise_nums = self.exercise_repository.get_exercise_number_for_level(level)
        db_exercise_numbers = [num[0] for num in exercise_nums]
        return db_exercise_numbers

    def get_exercise_text(self, exercise_number):
        exercise = self.exercise_repository.get_exercise(exercise_number)
        return exercise[0]

    def check_answer(self, answer, exercise_number):
        db_answer = self.exercise_repository.get_answer(exercise_number)[0]
        if float(answer) == db_answer:
            return "correct! :)"
        else:
            return "incorrect :("