import customtkinter as ctk
from colour import Color

from constants import *
from tab import Tab


class LEDsTab(Tab):
    def __init__(self, app: ctk.CTk, tab: ctk.CTkFrame) -> None:
        super().__init__(app, tab)
        self.led_switch_var = ctk.BooleanVar(value=True)
        self.led_color = Color("red")

    def setup(self) -> None:
        switch = ctk.CTkSwitch(
            master=self.tab,
            text="Off/On",
            command=self.toggle_led,
            variable=self.led_switch_var,
            onvalue=True,
            offvalue=False,
            font=(FONT_NAME, FONT_SIZE_LARGE),
        )
        switch.place(relx=0.5, rely=0.2, anchor="center")

        slider = self.make_color_slider(self.red_slider_event, 0.4, Color("red"))
        slider.set(self.led_color.get_red() * 255)
        self.red_slider = slider

        slider = self.make_color_slider(self.green_slider_event, 0.5, Color("green"))
        slider.set(self.led_color.get_green() * 255)
        self.green_slider = slider

        slider = self.make_color_slider(self.blue_slider_event, 0.6, Color("blue"))
        slider.set(self.led_color.get_blue() * 255)
        self.blue_slider = slider

        # Create a block to show the color of the LED
        color_preview = ctk.CTkLabel(
            master=self.tab,
            text=f"HEX {self.led_color.get_hex_l()}",
            font=(FONT_NAME, FONT_SIZE_LARGE),
            text_color=self.led_color.get_hex(),
        )
        color_preview.place(relx=0.5, rely=0.7, anchor="center")
        self.color_preview = color_preview

    def toggle_led(self):
        state = self.led_switch_var.get()

        for slider, color in [(self.red_slider, "red"), (self.green_slider, "green"), (self.blue_slider, "blue")]:
            slider.configure(
                state="normal" if state else "disabled",
                progress_color=color if state else "gray",
                button_color=("#3a7ebf", "#1f538d") if state else "gray" # The tuple is the default color as in set in the "dark-blue" theme
            )
        
        self.color_preview.configure(text_color=self.led_color.get_hex() if state else "gray")
    
    def red_slider_event(self, value: int):
        self.led_color.set_red(value / 255)
        self.update_color_preview()

    def green_slider_event(self, value: int):
        self.led_color.set_green(value / 255)
        self.update_color_preview()

    def blue_slider_event(self, value: int):
        self.led_color.set_blue(value / 255)
        self.update_color_preview()

    def make_color_slider(self, method, rely: float, color: Color) -> ctk.CTkSlider:
        slider = ctk.CTkSlider(
            master=self.tab,
            from_=0,
            to=255,
            width=self.app.winfo_screenwidth() * 0.4,
            height=50,
            command=method,
            progress_color=color.get_hex(),

        )
        slider.place(relx=0.5, rely=rely, anchor="center")

        return slider

    def update_color_preview(self) -> None:
        self.color_preview.configure(
            text=f"HEX {self.led_color.get_hex_l()}",
            text_color=self.led_color.get_hex(),
        )
