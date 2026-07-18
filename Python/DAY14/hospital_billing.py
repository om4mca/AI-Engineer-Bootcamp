#--------------------------------------------
# AI Engineer Bootcamp
# Day 14
# Program:  Hospital Billing System
# Author: Om Roy
# Date: 18-07-2026
#--------------------------------------------



class Person:
    """Base class representing a general person."""
    def __init__(self, name: str, age: int, mobile: str):
        self.name = name
        self.age = age
        self.mobile = mobile


class Patient(Person):
    """Child class representing a patient, inheriting personal details."""
    def __init__(self, name: str, age: int, mobile: str, patient_id: str, disease: str):
        super().__init__(name, age, mobile)
        self.patient_id = patient_id
        self.disease = disease


class Bill:
    """Class managing billing calculations, implementing strict Encapsulation."""
    def __init__(self, patient: Patient, consultation_fee: float, lab_fee: float, medicine_fee: float, discount: float = 0.0):
        self.patient = patient
        
        # Encapsulated Private Attributes (Hidden from direct external tampering)
        self.__consultation_fee = consultation_fee
        self.__lab_fee = lab_fee
        self.__medicine_fee = medicine_fee
        self.__discount = discount  # Flat discount amount
        self.__gst_rate = 0.18      # Fixed GST rate (18%)

    # Getter methods to access data safely if needed
    def get_consultation_fee(self): return self.__consultation_fee
    def get_lab_fee(self): return self.__lab_fee
    def get_medicine_fee(self): return self.__medicine_fee
    def get_discount(self): return self.__discount

    def calculate_subtotal(self) -> float:
        """Sums up raw charges minus the discount."""
        total_charges = self.__consultation_fee + self.__lab_fee + self.__medicine_fee
        # Ensure subtotal doesn't drop below zero if the discount is massive
        return max(0.0, total_charges - self.__discount)

    def calculate_gst(self) -> float:
        """Calculates 18% GST on the subtotal."""
        return self.calculate_subtotal() * self.__gst_rate

    def calculate_final_total(self) -> float:
        """Calculates the definitive total invoice cost."""
        return self.calculate_subtotal() + self.calculate_gst()

    def __str__(self) -> str:
        """
        Special method that overrides the default string representation of the object.
        Returns a beautifully formatted text receipt when you run print(bill_object).
        """
        receipt = []
        receipt.append("=" * 40)
        receipt.append("          CITY HEALTH HOSPITAL          ")
        receipt.append("             INVOICE RECEIPT            ")
        receipt.append("=" * 40)
        receipt.append(f"Patient ID : {self.patient.patient_id}")
        receipt.append(f"Name       : {self.patient.name} ({self.patient.age} yrs)")
        receipt.append(f"Mobile     : {self.patient.mobile}")
        receipt.append(f"Diagnosis  : {self.patient.disease}")
        receipt.append("-" * 40)
        receipt.append(f"Consultation Fee : {self.__consultation_fee:10.2f}")
        receipt.append(f"Laboratory Fee   : {self.__lab_fee:10.2f}")
        receipt.append(f"Medicine Charges : {self.__medicine_fee:10.2f}")
        receipt.append(f"Discount Allowed : -{self.__discount:9.2f}")
        receipt.append("-" * 40)
        receipt.append(f"Subtotal         : {self.calculate_subtotal():10.2f}")
        receipt.append(f"GST (18%)        : {self.calculate_gst():10.2f}")
        receipt.append("=" * 40)
        receipt.append(f"TOTAL AMOUNT DUE : {self.calculate_final_total():10.2f}")
        receipt.append("=" * 40)
        receipt.append("   Thank you. Wishing you a speedy recovery!  ")
        receipt.append("=" * 40)
        
        return "\n".join(receipt)


# --- Demonstration of the Billing System ---
if __name__ == "__main__":
    # 1. Register a Patient
    patient_record = Patient(
        name="Sudhir kumar", 
        age=42, 
        mobile="+1-555-0144", 
        patient_id="PT-9982", 
        disease="Acute Appendicitis"
    )

    # 2. Generate a Bill (Consultation=150, Lab=300, Meds=220, Discount=50)
    patient_bill = Bill(
        patient=patient_record,
        consultation_fee=150.00,
        lab_fee=300.00,
        medicine_fee=220.00,
        discount=50.00
    )

    # 3. Print the bill directly using the __str__() implementation
    print(patient_bill)
    
    # 4. Demonstrating Encapsulation protection:
    # Attempting to print patient_bill.__consultation_fee directly here will crash the script 
    # with an AttributeError because the financial properties are safely shielded inside the object!