import customtkinter as ctk
import subprocess

from constants import *
from tab import Tab


class AndroidAutoTab(Tab):
    def __init__(self, app: ctk.CTk, tab: ctk.CTkFrame) -> None:
        super().__init__(app, tab)

    def setup(self) -> None:
        start_butt = ctk.CTkButton(
            master=self.tab, text="Start", font=(FONT_NAME, FONT_SIZE_XXLARGE), command=self.start_android_auto
        )
        start_butt.place(relx=0.5, rely=0.5, anchor="center")
    
    # Starts the "autoapp" from OpenAuto
    def start_android_auto(self):
        subprocess.run(["sudo", "autoapp"])