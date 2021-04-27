from tkinter import Tk, ttk, constants, Toplevel
from .exercise_view import ExerciseView
from services.exercise_service import ExerciseService


class FrontPageView:
    def __init__(self, root, handle_log_out):
        self._root = root
        self._frame = None
        self._service = ExerciseService()
        self._handle_log_out = handle_log_out

        self._initialize()

    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack(fill=constants.X)
        

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(master=self._frame, text="Choose your exercise.")
        heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        db_levels = self._service.get_levels_list()
        for level in db_levels:
            ttk.Label(master=self._frame, text="Level {}".format(level)).grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
            db_exercise_number = self._service.get_exercise_number_list(level)
            for number in db_exercise_number:
                ttk.Button(master=self._frame, text="{}".format(number), command=lambda num=number: self._handle_button_click(num)).grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        ttk.Button(master=self._frame, text="Log out?", command=self._handle_log_out).grid(columnspan=2, sticky=constants.W, padx=5, pady=5)


    def _handle_button_click(self, exercise_number):
        exercise_window = Toplevel(self._frame)
        exercise_window.title("Exercise {}".format(exercise_number))

        exercise_ui = ExerciseView(exercise_window, exercise_number)
        exercise_ui.start()

        exercise_window.mainloop()

