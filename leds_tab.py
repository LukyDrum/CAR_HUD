import customtkinter as ctk
from colour import Color

from constants import *
from tab import Tab


class LEDsTab(Tab):
    def __init__(self, app: ctk.CTk, tab: ctk.CTkFrame) -> None:
        super().__init__(app, tab)
        self.led_switch_var = ctk.BooleanVar(value=True)
        self.led_color = Color("red")

    def setup(self) -> None:
        switch = ctk.CTkSwitch(
            master=self.tab,
            text="Off/On",
            command=self.toggle_led,
            variable=self.led_switch_var,
            onvalue=True,
            offvalue=False,
            font=(FONT_NAME, FONT_SIZE_LARGE),
        )
        switch.place(relx=0.5, rely=0.5, anchor="center")

    def toggle_led(self):
        pass
    