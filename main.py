import customtkinter as ctk
import subprocess


# Tabs of the app and the index of the current tab
tabs = ["Dashboard", "LEDs", "Android Auto"]
tab_index = 0

# Starts the "autoapp" from OpenAuto
def start_android_auto():
    subprocess.run(["sudo", "autoapp"])

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
FONT_NAME = "Roboto"
FONT_SIZE_NORMAL = 30
FONT_SIZE_LARGE = 50
FONT_SIZE_XXLARGE = 120
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("./themes/dark-blue.json")

# Initialize the app
app = ctk.CTk()
app.attributes('-fullscreen', True) # Set fullscreen
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
    prev_butt = ctk.CTkButton(tabview.tab(tab), text="←", font=(FONT_NAME, FONT_SIZE_LARGE), command=prev_tab)
    next_butt = ctk.CTkButton(tabview.tab(tab), text="→", font=(FONT_NAME, FONT_SIZE_LARGE), command=next_tab)

    prev_butt.place(relx=0.05, rely=0.5, anchor="center")
    next_butt.place(relx=0.95, rely=0.5, anchor="center")

# Android Auto tab
AA_tab = tabview.tab("Android Auto")
start_butt = ctk.CTkButton(AA_tab, text="Start", font=(FONT_NAME, FONT_SIZE_LARGE), command=start_android_auto)
start_butt.place(relx=0.5, rely=0.5, anchor="center")

# Dashboard tab
dashboard_tab = tabview.tab("Dashboard")
speed_label = ctk.CTkLabel(master=dashboard_tab, text="42", font=(FONT_NAME, FONT_SIZE_XXLARGE))
rpm_progress = ctk.CTkProgressBar(master=dashboard_tab, orientation="horizontal", width=screen_width//2, height=50)
speed_label.place(relx=0.5, rely=0.4, anchor="center")
rpm_progress.place(relx=0.5, rely=0.7, anchor="center")


if __name__ == "__main__":
    app.mainloop()