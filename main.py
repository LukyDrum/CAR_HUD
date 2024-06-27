import customtkinter as ctk
import os

from constants import *
import dashboard
# Tabs
from dashboard_tab import DashboardTab
from settings_tab import SettingsTab
from androidauto_tab import AndroidAutoTab
from leds_tab import LEDsTab

# Tabs of the app and the index of the current tab
tabs = ["Dashboard", "LEDs", "Android Auto", "Settings"]
tab_index = 0

# Dashboard object
dashboard = dashboard.Dashboard()
# Dummy values just for fun
dashboard.rpm = 800
dashboard.speed = 42


# Called when switing tabs using the top buttons
def tab_button_clicked():
    global tab_index, tabview
    new_tab = tabview.get()
    tab_index = tabs.index(new_tab)


# Cycle to the next tab
def next_tab():
    global tab_index, tabview
    tab_index = (tab_index + 1) % len(tabs)
    tabview.set(tabs[tab_index])


# Cycle to the previous tab
def prev_tab():
    global tab_index, tabview
    tab_index = (tab_index - 1) % len(tabs)
    tabview.set(tabs[tab_index])


# Setup appearence
ctk.set_appearance_mode("dark")
theme_path = os.path.dirname(__file__) + THEME
ctk.set_default_color_theme(theme_path)

# Initialize the app
app = ctk.CTk()
app.attributes("-fullscreen", True)  # Set fullscreen
app.title("Car HUD")

# Get the size of the screen
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

# Content of the app
tabview = ctk.CTkTabview(master=app, command=tab_button_clicked)
tabview.pack(padx=20, pady=20, fill="both", expand=True)

for tab in tabs:
    tabview.add(tab)
    # Place previous and next tab buttons
    prev_butt = ctk.CTkButton(
        tabview.tab(tab), text="←", font=(FONT_NAME, FONT_SIZE_LARGE), command=prev_tab
    )
    next_butt = ctk.CTkButton(
        tabview.tab(tab), text="→", font=(FONT_NAME, FONT_SIZE_LARGE), command=next_tab
    )

    prev_butt.place(relx=0.1, rely=0.5, anchor="center")
    next_butt.place(relx=0.9, rely=0.5, anchor="center")

# Android Auto tab
AA_tab = AndroidAutoTab(app, tabview.tab("Android Auto"))
AA_tab.setup()

# Dashboard tab
dashboard_tab = DashboardTab(app, tabview.tab("Dashboard"))
dashboard_tab.setup()

# Settings tab
settings_tab = SettingsTab(app, tabview.tab("Settings"))
settings_tab.setup()

# LEDs tab
leds_tab = LEDsTab(app, tabview.tab("LEDs"))
leds_tab.setup()

if __name__ == "__main__":
    dashboard_tab.update_loop()
    app.mainloop()
