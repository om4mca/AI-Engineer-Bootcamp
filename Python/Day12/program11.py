#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Mobile Class
# Author: Om Roy
# Date: 12-07-2026
#--------------------------------------------

class Mobile:
    def __init__(self, imei: str, brand: str, model: str, storage_capacity: int):
        """Initializes a smartphone device record."""
        self.imei = imei
        self.brand = brand
        self.model = model
        self.storage_capacity = storage_capacity  # Total space in GB
        
        # Internal states initialized by default
        self.battery_level = 100                  # Percent (100% full)
        self.available_storage = storage_capacity # Remaining space in GB
        self.installed_apps = []                  # Array keeping track of app strings

    def display_specs(self):
        """Prints out the current system status matrix of the phone."""
        print(f"\n--- System Status: {self.brand} {self.model} ---")
        print(f"IMEI Reference:    {self.imei}")
        print(f"Battery Capacity: {self.battery_level}%")
        print(f"Storage System:    {self.available_storage}GB free / {self.storage_capacity}GB total")
        print(f"Installed Apps:    {', '.join(self.installed_apps) if self.installed_apps else 'None'}")

    def install_app(self, app_name: str, app_size: float):
        """Installs an application if there is enough battery and storage room."""
        if self.battery_level < 15:
            print(f"[Installation Refused] Battery too low ({self.battery_level}%). Connect to a charger.")
            return

        if app_name in self.installed_apps:
            print(f"[Alert] '{app_name}' is already installed on this device.")
            return

        if app_size <= self.available_storage:
            self.installed_apps.append(app_name)
            self.available_storage -= app_size
            # The installation process drains a small amount of battery
            self.battery_level = max(0, self.battery_level - 3)
            print(f"[Success] Installed '{app_name}' ({app_size}GB). Battery dropped by 3%.")
        else:
            print(f"[Error] Out of space! Cannot install '{app_name}'. Requires {app_size}GB.")

    def use_app(self, app_name: str, duration_minutes: int):
        """Simulates running an application, which drains the device battery."""
        if app_name not in self.installed_apps:
            print(f"[Launch Error] '{app_name}' is not installed on this device.")
            return

        if self.battery_level <= 0:
            print("[System Shutdown] Phone is dead. Please charge the device.")
            return

        # Drains roughly 1% battery for every 5 minutes of usage
        drain_amount = max(1, duration_minutes // 5)
        self.battery_level = max(0, self.battery_level - drain_amount)
        print(f"[Active] Used '{app_name}' for {duration_minutes} mins. Drained {drain_amount}% battery.")
        
        if self.battery_level == 0:
            print("[Warning] Battery depleted to 0%. Device has powered down.")

    def charge_device(self, charge_amount: int):
        """Replenishes the mobile phone's battery reserve."""
        if charge_amount <= 0:
            print("[Error] Charge amount must be greater than zero.")
            return
            
        old_battery = self.battery_level
        self.battery_level = min(100, self.battery_level + charge_amount)
        print(f"[Power] Charging... Battery up from {old_battery}% to {self.battery_level}%.")


# --- Device Test Sequence ---
if __name__ == "__main__":
    print("Powering up mobile hardware architecture test pipeline...")

    # Instantiating custom smartphone instances
    phone1 = Mobile(imei="354629-01-123456-7", brand="Google", model="Pixel 9", storage_capacity=128)
    phone2 = Mobile(imei="449812-02-765432-1", brand="Apple", model="iPhone 17", storage_capacity=256)

    # Output fresh out-of-the-box specifications dashboard
    phone1.display_specs()

    print("\n" + "="*40 + "\nSimulating User Interactions...")

    # Modifying the first phone's internal properties dynamically via methods
    phone1.install_app("Spotify", app_size=1.5)
    phone1.install_app("Genshin Impact", app_size=32.0)
    
    # Running apps to drain resource attributes
    phone1.use_app("Spotify", duration_minutes=45)
    
    # Check updated live device state variables
    phone1.display_specs()

    print("\n" + "="*40 + "\nTesting Failure Conditions & Interlocks...")
    # Attempting to use a missing app package
    phone1.use_app("Netflix", duration_minutes=10)
    
    # Simulating extreme battery drainage to trigger a safety block
    phone1.battery_level = 10 
    phone1.install_app("Heavy Video Editor", app_size=5.0)  # Should fail due to battery threshold lock