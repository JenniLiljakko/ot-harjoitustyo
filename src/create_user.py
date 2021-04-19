from tkinter import ttk, constants, StringVar
from database import connection


class CreateUserView:
    def __init__(self, root):
        self._root = root
        self._username = None
        self._password = None
        self._label_var = None

    def start(self):
        self._label_var = StringVar()
        self._label_var.set("Create new username and password.")
        heading_label = ttk.Label(master=self._root, textvariable=self._label_var)

        username_label = ttk.Label(master=self._root, text="Username")
        self._username = ttk.Entry(master=self._root)

        password_label = ttk.Label(master=self._root, text="Password")
        self._password = ttk.Entry(master=self._root)

        button = ttk.Button(master=self._root, text="Create New User", command=self._handle_button_click)

        heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        username_label.grid(padx=5, pady=5)
        self._username.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        password_label.grid(padx=5, pady=5)
        self._password.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1, minsize=300)

    def _handle_button_click(self):
        username = self._username.get()
        password = self._password.get()

        db_username = connection.execute("SELECT username FROM users WHERE username=\'{}\'".format(username)).fetchone()
        if db_username is None:
            self._label_var.set("User created.")
            connection.execute("INSERT INTO users (username, password) VALUES (\'{}\',\'{}\')".format(username, password))
            self._root.destroy()
        else:
            self._label_var.set("User already exists.")

        
    

        
