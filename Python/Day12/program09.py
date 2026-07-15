#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Car Class
# Author: Om Roy
# Date: 12-07-2026
#--------------------------------------------
class Car:
    def __init__(self, vin: str, make: str, model: str, battery_capacity: int):
        """Initializes a new Electric Vehicle (EV) profile."""
        self.vin = vin
        self.make = make
        self.model = model
        self.battery_capacity = battery_capacity  # in kWh
        
        # Dynamic states initialized automatically
        self.charge_level = 100  # Starts fully charged at 100%
        self.current_speed = 0   # in mph
        self.is_running = False

    def display_dashboard(self):
        """Prints the current live instrument cluster readout."""
        status = "Engine ON" if self.is_running else "Engine OFF"
        print(f"\n--- Dashboard [{self.make} {self.model}] ---")
        print(f"VIN Reference:    {self.vin}")
        print(f"System State:     {status}")
        print(f"Current Speed:    {self.current_speed} mph")
        print(f"Battery Charge:   {self.charge_level}% ({self.battery_capacity} kWh pack)")

    def start_car(self):
        """Powers on the vehicle systems."""
        if not self.is_running:
            self.is_running = True
            print(f"[System] The {self.make} hums to life. Systems online.")
        else:
            print("[Warning] Vehicle is already powered on.")

    def accelerate(self, speed_increase: int):
        """Increases vehicle speed and dynamically discharges the battery state."""
        if not self.is_running:
            print("[Error] Cannot accelerate. Start the car first!")
            return

        if self.charge_level <= 0:
            print("[Critical] Out of energy! The car has safely stopped.")
            self.current_speed = 0
            return

        self.current_speed += speed_increase
        # Simulate energy depletion based on acceleration intensity
        energy_drain = max(1, int(speed_increase * 0.15))
        self.charge_level = max(0, self.charge_level - energy_drain)
        
        print(f"[Drive] Accelerating... Speed is now {self.current_speed} mph. Battery dropped by {energy_drain}%.")

    def brake(self):
        """Safely brings the vehicle to a stop."""
        if self.current_speed > 0:
            print(f"[Brake] Applying brakes. Safely slowing down from {self.current_speed} mph to 0 mph.")
            self.current_speed = 0
        else:
            print("[Info] Vehicle is already stationary.")


# --- Test Flight & State Tracking ---
if __name__ == "__main__":
    print("Connecting to Vehicle Onboard Diagnostic Link...")

    # Instantiating custom vehicle objects
    car1 = Car(vin="1V9EV_TEST00A1", make="Lucid", model="Air", battery_capacity=112)
    car2 = Car(vin="1V9EV_TEST00B2", make="Rivian", model="R1S", battery_capacity=135)

    # Inspect initial fresh-off-the-lot status
    car1.display_dashboard()

    print("\n" + "="*40 + "\nExecuting Drive Operations...")

    # Interacting with the first car object
    car1.start_car()
    car1.accelerate(30)  # Speeding up
    car1.accelerate(45)  # Stepping on it again
    
    # Check the digital dashboard to view updated state values
    car1.display_dashboard()

    # Safely wrap up the trip
    car1.brake()