#--------------------------------------------
# AI Engineer Bootcamp
# Day 15
# Program: Patient model
# Author: Om Roy
# Date: 20-07-2026
#--------------------------------------------

from datetime import date
from typing import Dict, Any, Optional

class Person:
    """Base class representing general personal details."""
    def __init__(self, name: str, age: int, gender: str, contact: str):
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        cleaned = value.strip().title()
        if not cleaned:
            raise ValueError("Name cannot be empty.")
        self._name = cleaned

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int):
        if not isinstance(value, int) or value <= 0 or value > 120:
            raise ValueError("Age must be an integer between 1 and 120.")
        self._age = value


class Patient(Person):
    """Patient class extending Person with clinical metadata."""
    def __init__(
        self,
        patient_id: str,
        name: str,
        age: int,
        gender: str,
        contact: str,
        ailment: str,
        assigned_doctor: str,
        admission_date: Optional[str] = None
    ):
        super().__init__(name, age, gender, contact)
        self.patient_id = patient_id
        self.ailment = ailment
        self.assigned_doctor = assigned_doctor
        self.admission_date = admission_date or date.today().isoformat()

    @property
    def patient_id(self) -> str:
        return self._patient_id

    @patient_id.setter
    def patient_id(self, value: str):
        cleaned = value.strip().upper()
        if not cleaned:
            raise ValueError("Patient ID cannot be empty.")
        self._patient_id = cleaned

    def to_dict(self) -> Dict[str, Any]:
        """Serializes patient instance into a dictionary format."""
        return {
            "patient_id": self._patient_id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "contact": self.contact,
            "ailment": self.ailment,
            "assigned_doctor": self.assigned_doctor,
            "admission_date": self.admission_date,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Patient":
        """Factory method to construct a Patient object from a dictionary."""
        return cls(
            patient_id=data["patient_id"],
            name=data["name"],
            age=data["age"],
            gender=data["gender"],
            contact=data["contact"],
            ailment=data["ailment"],
            assigned_doctor=data["assigned_doctor"],
            admission_date=data.get("admission_date")
        )

    def __repr__(self) -> str:
        return (f"Patient(ID='{self.patient_id}', Name='{self.name}', "
                f"Ailment='{self.ailment}', Doctor='{self.assigned_doctor}')")


# Example Usage
if __name__ == "__main__":
    patient = Patient(
        patient_id="P101",
        name="John Doe",
        age=34,
        gender="Male",
        contact="+1-555-0199",
        ailment="Acute Appendicitis",
        assigned_doctor="Dr. Smith"
    )
    
    print(patient)
    print("Serialized Dict:", patient.to_dict())