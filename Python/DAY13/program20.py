#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Mini OOP Challenge
# Author: Om Roy
# Date: 17-07-2026
#--------------------------------------------

# smart_home.py

class SmartDevice:
    """Base class for all smart home hardware elements."""
    def __init__(self, device_name: str):
        self.device_name = device_name
        self.is_on = False  # All devices start turned off by default

    def toggle_power(self):
        """Switches the device's electrical power state."""
        self.is_on = not self.is_on
        status = "ON" if self.is_on else "OFF"
        print(f"{self.device_name} is now {status}.")


class SmartLight(SmartDevice):
    """Child class specializing in dimmable light bulbs."""
    def __init__(self, device_name: str, brightness: int = 50):
        # Route the device naming logic up to the base SmartDevice init
        super().__init__(device_name)
        # Handle specialized light settings
        self.brightness = brightness

    def set_brightness(self, level: int):
        """Updates brightness ensuring values stay locked between 1 and 100."""
        if 1 <= level <= 100:
            self.brightness = level
            print(f"[{self.device_name}] Brightness adjusted to {self.brightness}%.")
        else:
            print(f"[Setting Error] Brightness must fall between 1% and 100%.")

    def toggle_power(self):
        """
        Overrides the standard toggle behavior.
        Injects brightness status metrics only when the light system boots up.
        """
        # Run standard boolean toggle logic from parent class
        super().toggle_power()
        
        # Add specialized output context based on state
        if self.is_on:
            print(f"-> Glow Intensity: {self.brightness}% illumination capacity.")


# --- Execution Demonstration ---
if __name__ == "__main__":
    # Initialize light item setup
    living_room_light = SmartLight("Living Room Bulb", brightness=75)
    
    print("1. Toggling Light On:")
    living_room_light.toggle_power() 
    # Output confirms power state change + reads custom brightness metrics

    print("\n2. Adjusting Brightness Details:")
    living_room_light.set_brightness(90)
    living_room_light.set_brightness(150) # Intentionally triggering safe bounds protection
    
    print("\n3. Toggling Light Off:")
    living_room_light.toggle_power()
    # Safely switches off without cluttering output console with brightness data