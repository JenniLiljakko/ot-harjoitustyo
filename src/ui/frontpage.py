from tkinter import Tk, ttk, constants, Toplevel
from database import connection
from .exercise_view import ExerciseView


class FrontPageView:
    def __init__(self, root):
        self._root = root
        

    def start(self):
        heading_label = ttk.Label(master=self._root, text="Choose your exercise.")
        heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        db_levels = connection.execute("SELECT DISTINCT exercise_level FROM exercises").fetchall()
        for level in db_levels:
            ttk.Label(master=self._root, text="Level {}".format(level[0])).grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
            db_exercise_number = connection.execute("SELECT exercise_number FROM exercises WHERE exercise_level = {}".format(level[0])).fetchall()
            for number in db_exercise_number:
                ttk.Button(master=self._root, text="{}".format(number[0]), command=lambda num=number[0]: self._handle_button_click(num)).grid(columnspan=2, sticky=constants.W, padx=5, pady=5)

    def _handle_button_click(self, exercise_number):
        print(exercise_number)
        exercise_window = Toplevel(self._root)
        exercise_window.title("Exercise {}".format(exercise_number))

        exercise_ui = ExerciseView(exercise_window, exercise_number)
        exercise_ui.start()

        exercise_window.mainloop()


window = Tk()
window.title("Welcome to exercise-generator 1.0")

ui = FrontPageView(window)
ui.start()

window.mainloop()
