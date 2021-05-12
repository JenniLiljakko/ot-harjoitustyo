from tkinter import ttk, constants, StringVar, Toplevel
from services.user_service import UserService
from .create_user import CreateUserView


class LoginView:
    def __init__(self, root, handle_access):
        self._root = root
        self._handle_access = handle_access
        self._username = None
        self._password = None
        self._label_var = None
        self._frame = None

        self._initialize()

    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack(fill=constants.X)


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._label_var = StringVar()
        self._label_var.set("Type your username and password.")
        heading_label = ttk.Label(master=self._frame, textvariable=self._label_var)

        username_label = ttk.Label(master=self._frame, text="Username")
        self._username = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Password")
        self._password = ttk.Entry(master=self._frame)

        login_button = ttk.Button(master=self._frame, text="Login", \
                                    command=self._handle_button_click)
        new_user_button = ttk.Button(master=self._frame, text="Create a new user?", \
                                    command=self._handle_new_user_button_click)

        heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        username_label.grid(padx=5, pady=5)
        self._username.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        password_label.grid(padx=5, pady=5)
        self._password.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        login_button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        new_user_button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1, minsize=300)

    def _handle_button_click(self):
        username = self._username.get()
        password = self._password.get()

        service = UserService()
        message = service.login(username, password)
        self._label_var.set(message)
        if message == "Welcome":
            self._handle_access()

    def _handle_new_user_button_click(self):
        create_user_window = Toplevel(self._frame)
        create_user_window.title("Create User")

        create_user_ui = CreateUserView(create_user_window)
        create_user_ui.start()

        create_user_window.mainloop()
