import customtkinter as ctk
import subprocess
import os

from constants import *
from tab import Tab


class SettingsTab(Tab):
    def __init__(self, app: ctk.CTk, tab: ctk.CTkFrame) -> None:
        super().__init__(app, tab)
        self.theme_switch_var = ctk.StringVar(value=DARK)

    def setup(self) -> None:
        switch = ctk.CTkSwitch(
            master=self.tab,
            text="Light/Dark Theme",
            command=self.switch_theme,
            variable=self.theme_switch_var,
            onvalue=DARK,
            offvalue=LIGHT,
            font=(FONT_NAME, FONT_SIZE_LARGE),
        )
        switch.place(relx=0.5, rely=0.3, anchor="center")

        # Update button
        update_button = ctk.CTkButton(
            master=self.tab,
            text="Update",
            font=(FONT_NAME, FONT_SIZE_LARGE),
            command=self.update,
        )
        update_button.place(relx=0.5, rely=0.5, anchor="center")

        # Exit button
        exit_button = ctk.CTkButton(
            master=self.tab,
            text="Exit",
            font=(FONT_NAME, FONT_SIZE_LARGE),
            command=self.app.destroy,
        )
        exit_button.place(relx=0.5, rely=0.7, anchor="center")


    # Switch theme from light to dark and viceversa
    def switch_theme(self):
        ctk.set_appearance_mode(self.theme_switch_var.get())

    # Call update script and restart the app
    def update(self):
        path = os.path.dirname(__file__)

        subprocess.call(["sh", path + "/update.sh"])
        subprocess.call(["python3", path + "/main.py"])
        self.app.destroy()