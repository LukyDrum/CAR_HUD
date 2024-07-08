import customtkinter as ctk

from constants import *
from tab import Tab


class MusicTab(Tab):
    def __init__(self, app: ctk.CTk, tab: ctk.CTkFrame) -> None:
        super().__init__(app, tab)

    def setup(self) -> None:
        pass
