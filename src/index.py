from tkinter import Tk
from ui.login import LoginView

window = Tk()
window.title("Login")

ui = LoginView(window)
ui.start()

window.mainloop()
