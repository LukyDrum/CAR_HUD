import customtkinter as ctk


class Tab:
    def __init__(self, app: ctk.CTk, tab: ctk.CTkFrame) -> None:
        self.app = app
        self.tab = tab

    def setup(self) -> None:
        pass