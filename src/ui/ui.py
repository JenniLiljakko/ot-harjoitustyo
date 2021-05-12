from ui.login import LoginView
from ui.frontpage  import FrontPageView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._handle_access
        )

        self._current_view.pack()

    def _handle_access(self):
        self._hide_current_view()

        self._current_view = FrontPageView(
            self._root,
            self._show_login_view
        )

        self._current_view.pack()
        