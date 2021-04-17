from tkinter import Tk
from login import LoginView

window = Tk()
window.title("Login")

ui = LoginView(window)
ui.start()

window.mainloop()
