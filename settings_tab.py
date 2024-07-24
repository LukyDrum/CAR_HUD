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
        controls = []

        switch = ctk.CTkSwitch(
            master=self.tab,
            text="Light/Dark Theme",
            command=self.switch_theme,
            variable=self.theme_switch_var,
            onvalue=DARK,
            offvalue=LIGHT,
            font=(FONT_NAME, FONT_SIZE_LARGE),
        )
        controls.append(switch)

        # Update button
        update_button = ctk.CTkButton(
            master=self.tab,
            text="Update",
            font=(FONT_NAME, FONT_SIZE_LARGE),
            command=self.update,
        )
        self.update_button = update_button
        controls.append(update_button)

        # Restart button
        restart_button = ctk.CTkButton(
            master=self.tab,
            text="Restart",
            font=(FONT_NAME, FONT_SIZE_LARGE),
            command=self.restart,
        )
        controls.append(restart_button)

        # Disconnect Bluetooth button
        disconnect_bt_button = ctk.CTkButton(
            master=self.tab,
            text="BT Disconnect",
            font=(FONT_NAME, FONT_SIZE_LARGE),
            command=self.disconnect_bt,
        )
        controls.append(disconnect_bt_button)

        # Exit button
        exit_button = ctk.CTkButton(
            master=self.tab,
            text="Exit",
            font=(FONT_NAME, FONT_SIZE_LARGE),
            command=self.exit,
        )
        controls.append(exit_button)

        y = 0.1
        for control in controls:
            control.place(relx=0.5, rely=y, anchor="center")
            y += 0.2


    # Switch theme from light to dark and viceversa
    def switch_theme(self):
        ctk.set_appearance_mode(self.theme_switch_var.get())

    # Call update script and restart the app
    def update(self):
        path = os.path.dirname(__file__)

        # Change text on button
        self.update_button.configure(text="Updating...")

        subprocess.call(["sh", path + "/update.sh"])
        subprocess.call(["python3", path + "/main.py"])
        self.app.destroy()

    # This will restart the app
    def restart(self):
        path = os.path.dirname(__file__)

        subprocess.call(["python3", path + "/main.py"])
        self.app.destroy()

    def disconnect_bt(self):
        path = os.path.dirname(__file__)

        subprocess.call(["sh", path + "/bluetooth/disconnect.sh"])

    # This will exit the app
    def exit(self):
        self.app.destroy()