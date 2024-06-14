import customtkinter as ctk
import subprocess


# Tabs of the app and the index of the current tab
tabs = ["Dashboard", "LEDs", "Android Auto"]
tab_index = 0

def start_android_auto():
    subprocess.run(["sudo", "autoapp"])

def tab_button_clicked(tab: str):
    global tab_index
    tab_index = tabs.index(tab)

def next_tab():
    global tab_index, tabview
    tab_index = (tab_index + 1) % len(tabs)
    tabview.set(tabs[tab_index])

def prev_tab():
    global tab_index, tabview
    tab_index = (tab_index - 1) % len(tabs)
    tabview.set(tabs[tab_index])


FONT_NAME = "Roboto"
FONT_SIZE_NORMAL = 30
FONT_SIZE_LARGE = 50
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("./themes/dark-blue.json")


app = ctk.CTk()
app.attributes('-fullscreen', True) # Set fullscreen
app.title("Car HUD")

# Content
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



if __name__ == "__main__":
    app.mainloop()