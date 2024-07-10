import customtkinter as ctk
import time

from constants import *
from bluetooth.bluetooth_player import BluetoothPlayer
from utils import limit_text

class InfoPanel:
    def __init__(self, app: ctk.CTk, bt_player: BluetoothPlayer) -> None:
        self.app = app
        self.bt_player = bt_player

        self.frame = ctk.CTkFrame(master=self.app, width=self.app.winfo_screenwidth(), fg_color="transparent", height=self.app.winfo_screenheight() * 0.075)
        self.frame.pack()

    def setup(self) -> None:
        # Show label with current time
        clock = ctk.CTkLabel(master=self.frame, text="00:00", font=(FONT_NAME, FONT_SIZE_LARGER))
        clock.place(relx=0.5, rely=0.5, anchor="center")
        self.clock = clock

        # Show label with the name of the connected device
        bt_label = ctk.CTkLabel(master=self.frame, text="BT", font=(FONT_NAME, FONT_SIZE_NORMAL))
        bt_label.place(relx=0.01, rely=0.5, anchor="w")
        self.bt_label = bt_label


    def update_loop(self) -> None:
        self.clock.configure(text=time.strftime("%H:%M"))

        if self.bt_player.device is not None:
            self.bt_label.configure(text= limit_text(f"BT: {self.bt_player.device.name}", 25))
        else:
            self.bt_label.configure(text="BT not connected")

        # Update each second
        self.app.after(1000, self.update_loop)