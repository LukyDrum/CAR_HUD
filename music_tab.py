import customtkinter as ctk
import threading

from constants import *
from tab import Tab
from bluetooth.bluetooth_player import BluetoothPlayer
from utils import limit_text


class MusicTab(Tab):
    def __init__(self, app: ctk.CTk, tab: ctk.CTkFrame) -> None:
        super().__init__(app, tab)

        self.player = BluetoothPlayer()
        self.butt_size = FONT_SIZE_XLARGE

        self.thread = None

    def setup(self) -> None:
        # Song info
        song_title = ctk.CTkLabel(
            master=self.tab,
            text="Deatwish",
            font=(FONT_NAME, FONT_SIZE_XLARGE),
        )
        song_title.place(relx=0.5, rely=0.2, anchor="center")
        self.song_title = song_title

        song_artist = ctk.CTkLabel(
            master=self.tab,
            text="Daft Punk",
            font=(FONT_NAME, FONT_SIZE_LARGE),
        )
        song_artist.place(relx=0.5, rely=0.4, anchor="center")
        self.song_artist = song_artist


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
            command=self.player.next,
        )
        next_butt.place(relx=0.7, rely=0.7, anchor="center")

        play_pause_butt = ctk.CTkButton(
            master=self.tab,
            text="⏵",
            font=(FONT_NAME, self.butt_size),
            command=self.player.play_pause,
        )
        play_pause_butt.place(relx=0.5, rely=0.7, anchor="center")
        self.play_pause_butt = play_pause_butt

    def update_loop(self) -> None:
        thread = threading.Thread(target= self.update_async)
        thread.start()

        self.thread = thread

        self.app.after(UPDATE_TIME, self.update_loop)

    def update_async(self) -> None:
        self.player.update_device()

        song_info = self.player.get_song_info()

        # Limit title to 30 chars and artist to 25
        self.song_title.configure(text=limit_text(song_info.title, 30))
        self.song_artist.configure(text=limit_text(song_info.artist, 25))

        self.player.update_playing_status()

        if self.player.playing:
            self.play_pause_butt.configure(text="⏸")
        else:
            self.play_pause_butt.configure(text="⏵")

    def end_thread(self) -> None:
        self.thread.join()