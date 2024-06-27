import customtkinter as ctk

from constants import *
from tab import Tab


class DashboardTab(Tab):
    def __init__(self, app: ctk.CTk, tab: ctk.CTkFrame) -> None:
        super().__init__(app, tab)

    def setup(self) -> None:
        dash_speed_label = ctk.CTkLabel(
            master=self.tab, text="42", font=(FONT_NAME, FONT_SIZE_XXLARGE)
        )
        dash_rpm_progress = ctk.CTkProgressBar(
            master=self.tab, orientation="horizontal", width=self.app.winfo_screenwidth() // 2, height=50
        )
        dash_speed_label.place(relx=0.5, rely=0.4, anchor="center")
        dash_rpm_progress.place(relx=0.5, rely=0.7, anchor="center")