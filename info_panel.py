import customtkinter as ctk
import time

from constants import *


class InfoPanel:
    def __init__(self, app: ctk.CTk) -> None:
        self.app = app

        self.frame = ctk.CTkFrame(master=self.app, width=self.app.winfo_screenwidth(), fg_color="transparent")
        self.frame.pack()

    def setup(self) -> None:
        clock = ctk.CTkLabel(master=self.frame, text="00:00", font=(FONT_NAME, FONT_SIZE_XLARGE))
        clock.pack()

        self.clock = clock

    def update_loop(self) -> None:
        self.clock.configure(text=time.strftime("%H:%M"))

        self.app.after(1000, self.update_loop)