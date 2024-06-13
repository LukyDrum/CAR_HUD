import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("./themes/dark-blue.json")

app = ctk.CTk()
app.attributes('-fullscreen', True) # Set fullscreen
app.title("Car HUD")

# Content
tabview = ctk.CTkTabview(master=app)
tabview.pack(padx=20, pady=20, fill="both", expand=True)

tabview.add("Dashboard")
tabview.add("LEDs")
tabview.add("Android Auto")

tabview.set("Dashboard")


if __name__ == "__main__":
    app.mainloop()