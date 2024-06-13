import customtkinter as ctk
import subprocess


def start_android_auto():
    subprocess.run(["sudo", "autoapp"])

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("./themes/dark-blue.json")

app = ctk.CTk()
app.attributes('-fullscreen', True) # Set fullscreen
app.title("Car HUD")

# Content
tabview = ctk.CTkTabview(master=app)
tabview.pack(padx=20, pady=20, fill="both", expand=True)

dash_tab = tabview.add("Dashboard")
leds_tab = tabview.add("LEDs")
AA_tab = tabview.add("Android Auto")

tabview.set("Dashboard")


# Android Auto tab
start_butt = ctk.CTkButton(AA_tab, text="Start", command=start_android_auto)
start_butt.place(relx=0.5, rely=0.5, anchor="center")



if __name__ == "__main__":
    app.mainloop()