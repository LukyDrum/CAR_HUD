import customtkinter as ctk

from constants import *
from tab import Tab
from bluetooth.bluetooth_player import BluetoothPlayer


class MusicTab(Tab):
    def __init__(self, app: ctk.CTk, tab: ctk.CTkFrame) -> None:
        super().__init__(app, tab)

        self.player = BluetoothPlayer()
        self.butt_size = FONT_SIZE_XLARGE

    def setup(self) -> None:
        # Song info
        song_title = ctk.CTkLabel(
            master=self.tab,
            text="Deatwish",
            font=(FONT_NAME, FONT_SIZE_XLARGE),
        )
        song_title.place(relx=0.5, rely=0.3, anchor="center")

        song_artist = ctk.CTkLabel(
            master=self.tab,
            text="Daft Punk",
            font=(FONT_NAME, FONT_SIZE_LARGE),
        )
        song_artist.place(relx=0.5, rely=0.4, anchor="center")


        # Control buttons
        previous_butt = ctk.CTkButton(
            master=self.tab,
            text="⏮",
            font=(FONT_NAME, self.butt_size),
            command=self.player.previous,
        )
        previous_butt.place(relx=0.3, rely=0.7, anchor="center")
        
        next_butt = ctk.CTkButton(
            master=self.tab,
            text="⏭",
            font=(FONT_NAME, self.butt_size),
            command=self.player.previous,
        )
        next_butt.place(relx=0.7, rely=0.7, anchor="center")

        play_pause_butt = ctk.CTkButton(
            master=self.tab,
            text="⏯",
            font=(FONT_NAME, self.butt_size),
            command=self.player.play_pause,
        )
        play_pause_butt.place(relx=0.5, rely=0.7, anchor="center")

    def update_loop(self) -> None:
        self.player.update_device()

        self.app.after(UPDATE_TIME, self.update_loop)