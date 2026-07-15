#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Update Object Data
# Author: Om Roy
# Date: 15-07-2026
#--------------------------------------------
class RentalItem:
    def __init__(self, item_id: str, title: str, daily_rate: float):
        """Initializes a new rental media object inventory asset."""
        self.item_id = item_id
        self.title = title
        self.daily_rate = daily_rate
        
        # Internal mutable operational tracking variables
        self.status = "Available"
        self.total_revenue_generated = 0.0

    def display_status(self):
        """Prints out the current execution tracking metrics sheet."""
        print(f"  [{self.item_id}] Title: {self.title:<22} | Status: {self.status:<11} | Revenue: ${self.total_revenue_generated:,.2f}")

    def process_checkout(self):
        """Updates internal status fields after state condition verification."""
        if self.status == "Available":
            # State Update Pattern 1: Direct Status Flag Shift
            self.status = "Rented"
            print(f"[System Log] Update Approved: '{self.title}' has been marked as RENTED.")
        else:
            print(f"[System Error] Update Denied: '{self.title}' is already checked out.")

    def process_return_and_bill(self, days_rented: int):
        """Updates object attributes, calculating metrics and accumulating stats safely."""
        if self.status != "Rented":
            print(f"[System Error] Update Denied: '{self.title}' is not currently logged as rented.")
            return

        if days_rented <= 0:
            print("[Validation Error] Update Denied: Rental duration metrics must be positive.")
            return

        # State Update Pattern 2: Mathematical Accumulation
        cost = self.daily_rate * days_rented
        self.total_revenue_generated += cost
        self.status = "Available"
        
        print(f"[System Log] Update Approved: '{self.title}' returned safely.")
        print(f"  Calculated charge: ${cost:,.2f} tracking to asset inventory ledger accounts.")


# --- Object Mutation Runtime Engine ---
if __name__ == "__main__":
    print("Opening Media Rental State Processing Engine...\n")

    # 1. Instantiate target inventory asset tracking object references
    movie1 = RentalItem("MOV-991", "Interstellar", daily_rate=3.99)
    movie2 = RentalItem("MOV-442", "Spirited Away", daily_rate=2.50)

    print("Initial System State Baseline Matrix:")
    movie1.display_status()
    movie2.display_status()

    print("\n" + "="*55 + "\nProcessing Action Matrix (Mutating Object States)...")
    # 2. Triggering data state transitions through methods
    movie1.process_checkout()
    
    # 3. Running conditional rules checks (should trigger block warning)
    movie1.process_checkout() 

    print("\n" + "="*55 + "\nProcessing Returns & Financial Ledger Mutations...")
    # 4. Closing workflow loops and incrementing numerical parameters safely
    movie1.process_return_and_bill(days_rented=5)  # 5 days * $3.99 = $19.95 loaded
    
    print("\nTesting Malformed Metric Data Safeguards...")
    # 5. Verifying internal sanity boundary code gates
    movie1.process_checkout()
    movie1.process_return_and_bill(days_rented=-3) # Should trigger data anomaly error blocks

    print("\n" + "="*55 + "\nFinal Verified System Inventory Census:")
    # Confirming state persistence variables match execution records perfectly
    movie1.display_status()
    movie2.display_status()