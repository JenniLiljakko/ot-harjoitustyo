from tkinter import Tk, ttk, constants, StringVar, Toplevel
from database import connection


class ExerciseView:
    def __init__(self, root, exercise_number):
        self._root = root
        self._exercise_number = exercise_number
        self._label_var = None

    def start(self):
        top_label = ttk.Label(master=self._root, text="Solve the following exercise")
        db_exercise = connection.execute("SELECT exercise FROM exercises WHERE exercise_number={}".format(self._exercise_number)).fetchone()
        exercise_label = ttk.Label(master=self._root, wraplength=250, text=db_exercise[0])
        self._answer_field = ttk.Entry(master=self._root)
        submit_button = ttk.Button(master=self._root, text="Submit", command=self._handle_button_click)

        self._label_var = StringVar()
        self._label_var.set("")
        bottom_label = ttk.Label(master=self._root, textvariable=self._label_var)

        top_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        exercise_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        self._answer_field.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        submit_button.grid(columnspan=4, sticky=(constants.E, constants.W), padx=5, pady=5)
        
        bottom_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)

    def _handle_button_click(self):
        answer = self._answer_field.get()
        db_answer = connection.execute("SELECT answer FROM exercises WHERE exercise_number={}".format(self._exercise_number)).fetchone()
        if float(answer)==db_answer[0]:
            self._label_var.set("correct! :)")
        else:
            self._label_var.set("incorrect :(")

    
window = Tk()
window.title("Exercise")

ui = ExerciseView(window, 1)
ui.start()

window.mainloop()
