from tkinter import Tk
from ui.ui import UI

window = Tk()
window.title("Exercise generator")

ui = UI(window)
ui.start()

window.mainloop()
