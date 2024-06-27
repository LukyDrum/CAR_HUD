from colour import Color

RPM_MAX = 7000
SPEED_MAX = 250

BLUE = Color("blue")
RED = Color("red")
COLOR_SAMPLES_COUNT = 200
COLOR_LIST = list(BLUE.range_to(RED, COLOR_SAMPLES_COUNT))

class Dashboard:
    def __init__(self):
        self.speed: int = 0 # In km/h
        self.rpm: int = 0

    # Get adequate color based on current RPM
    def get_rpm_color(self) -> Color:
        index = int((self.rpm / RPM_MAX) * COLOR_SAMPLES_COUNT)
        if index >= COLOR_SAMPLES_COUNT:
            index = COLOR_SAMPLES_COUNT - 1
        return COLOR_LIST[index]
    
    # Get percentage of current RPM in respect to the RPM_MAX value
    def get_rpm_percentage(self) -> float:
        return self.rpm / RPM_MAX
    
    # Return speed in km per hour
    def get_kmh(self) -> int:
        return self.speed
    
    # Return speed in miles per hour
    def get_mph(self) -> int:
        return int(self.speed * 0.621371)