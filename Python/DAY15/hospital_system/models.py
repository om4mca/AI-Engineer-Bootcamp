"""Domain models for Person and Patient using Object-Oriented Design."""

class Person:
    """Base class representing a general individual."""
    def __init__(self, name: str, age: int, gender: str, contact: str):
        self._name = name.strip().title()
        self._age = age
        self._gender = gender.strip().capitalize()
        self._contact = contact.strip()

    # Getters and setters (Encapsulation)
    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    @property
    def gender(self) -> str:
        return self._gender

    @property
    def contact(self) -> str:
        return self._contact

    def get_details(self) -> dict:
        return {
            "Name": self._name,
            "Age": self._age,
            "Gender": self._gender,
            "Contact": self._contact
        }


class Patient(Person):
    """Patient class inheriting from Person, adding medical metadata."""
    def __init__(self, patient_id: str, name: str, age: int, gender: str, contact: str, ailment: str, doctor: str):
        super().__init__(name, age, gender, contact)
        self.__patient_id = patient_id.upper().strip()
        self.ailment = ailment.strip().title()
        self.doctor = doctor.strip().title()

    @property
    def patient_id(self) -> str:
        return self.__patient_id

    def to_dict(self) -> dict:
        """Converts model to dictionary format for file serialization."""
        data = super().get_details()
        data.update({
            "patient_id": self.__patient_id,
            "ailment": self.ailment,
            "doctor": self.doctor
        })
        return data

    @classmethod
    def from_dict(cls, data: dict) -> "Patient":
        """Factory method to construct a Patient object from JSON data."""
        return cls(
            patient_id=data["patient_id"],
            name=data["Name"],
            age=data["Age"],
            gender=data["Gender"],
            contact=data["Contact"],
            ailment=data["ailment"],
            doctor=data["doctor"]
        )

    def __str__(self) -> str:
        return (f"[{self.__patient_id}] {self.name} | Age: {self.age} | "
                f"Gender: {self.gender} | Contact: {self.contact} | "
                f"Ailment: {self.ailment} | Doctor: {self.doctor}")