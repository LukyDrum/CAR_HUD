import customtkinter as ctk

from constants import *
from tab import Tab
from dashboard import Dashboard


class DashboardTab(Tab):
    def __init__(self, app: ctk.CTk, tab: ctk.CTkFrame) -> None:
        super().__init__(app, tab)
        self.dashboard = Dashboard()

    def setup(self) -> None:
        speed_label = ctk.CTkLabel(
            master=self.tab, text=self.dashboard.get_kmh(), font=(FONT_NAME, FONT_SIZE_XXLARGE)
        )
        rpm_progress = ctk.CTkProgressBar(
            master=self.tab, orientation="horizontal", width=self.app.winfo_screenwidth() // 2, height=50
        )
        speed_label.place(relx=0.5, rely=0.4, anchor="center")
        rpm_progress.place(relx=0.5, rely=0.7, anchor="center")

        self.speed_label = speed_label
        self.rpm_progress = rpm_progress

    def update_loop(self) -> None:
        self.speed_label.configure(text=self.dashboard.get_kmh())

        self.rpm_progress.set(self.dashboard.get_rpm_percentage())
        self.rpm_progress.configure(progress_color=self.dashboard.get_rpm_color().get_hex())

        self.app.after(UPDATE_TIME, self.update_loop)