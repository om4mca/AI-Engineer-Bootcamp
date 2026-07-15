#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Multiple Objects
# Author: Om Roy
# Date: 15-07-2026
#--------------------------------------------

class Device:
    def __init__(self, device_id: str, type: str, status: str):
        """Initializes an internet-of-things (IoT) smart device object."""
        self.device_id = device_id
        self.type = type
        self.status = status  # "Online", "Offline", or "Maintenance"

    def get_summary(self) -> str:
        """Returns a string summary of the object instance."""
        return f"[{self.device_id}] Type: {self.type:<12} | Status: {self.status}"

    def trigger_reboot(self):
        """Simulates executing an instance-level process change."""
        if self.status == "Offline":
            print(f"  [System] Reboot signal sent to {self.device_id}... Booting up.")
            self.status = "Online"
        else:
            print(f"  [System] {self.device_id} is already functional. Bypassing reboot.")


# --- Batch Processing & Management Ecosystem ---
if __name__ == "__main__":
    print("Initializing IoT Device Control Command Center...\n")

    # 1. Storing Multiple Objects inside a List Container
    device_inventory = [
        Device("DEV-101", "Thermostat", "Online"),
        Device("DEV-102", "Security Cam", "Offline"),
        Device("DEV-103", "Smart Lock", "Online"),
        Device("DEV-104", "Light Panel", "Offline"),
    ]

    # 2. Batch Processing: Iterate over every object using a loop
    print("--- Current Network Census ---")
    for device in device_inventory:
        print(device.get_summary())

    print("\n" + "="*50 + "\nAutomated Network Remediation Sequence...")
    # 3. Filtering & Targeting Actions on specific objects based on states
    print("Detecting unresponsive hardware nodes...")
    for device in device_inventory:
        if device.status == "Offline":
            print(f"\n⚠️ Alert: {device.device_id} is down!")
            device.trigger_reboot()  # Mutate state on specific object instance

    print("\n" + "="*50 + "\nPost-Remediation Verification Matrix")
    # 4. Confirming state shifts across all collection members
    for device in device_inventory:
        print(device.get_summary())


    print("\n" + "="*50 + "\nAdvanced Lookup: Storing Objects in a Dictionary")
    # 5. Using Key-Value Pairs for Instant, Direct Object Querying
    # This maps a unique identifier (Device ID) directly to the complete object block
    network_map = {device.device_id: device for device in device_inventory}

    # Query an exact instance target immediately in O(1) time complexity
    target_id = "DEV-102"
    if target_id in network_map:
        print(f"Direct Lookup Success for target '{target_id}':")
        # Pull the object out of the dictionary map and access its method variables
        print(f"  Live Telemetry Status -> {network_map[target_id].status}")