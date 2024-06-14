import customtkinter as ctk
import subprocess


# Tabs of the app and the index of the current tab
tabs = ["Dashboard", "LEDs", "Android Auto"]
tab_index = 0

def start_android_auto():
    subprocess.run(["sudo", "autoapp"])


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("./themes/dark-blue.json")

FONT_NAME = "Roboto"

app = ctk.CTk()
app.attributes('-fullscreen', True) # Set fullscreen
app.title("Car HUD")

# Content
tabview = ctk.CTkTabview(master=app)
tabview.pack(padx=20, pady=20, fill="both", expand=True)

for tab in tabs:
    tabview.add(tab)

# Android Auto tab
AA_tab = tabview.tab("Android Auto")
start_butt = ctk.CTkButton(AA_tab, text="Start", font=(FONT_NAME, 50), command=start_android_auto)
start_butt.place(relx=0.5, rely=0.5, anchor="center")



if __name__ == "__main__":
    app.mainloop()