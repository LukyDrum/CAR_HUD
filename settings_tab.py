import customtkinter as ctk

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
        switch.place(relx=0.5, rely=0.4, anchor="center")
        exit_button = ctk.CTkButton(
            master=self.tab,
            text="Exit",
            font=(FONT_NAME, FONT_SIZE_LARGE),
            command=self.app.destroy,
        )
        exit_button.place(relx=0.5, rely=0.6, anchor="center")

    # Switch theme from light to dark and viceversa
    def switch_theme(self):
        ctk.set_appearance_mode(self.theme_switch_var.get())