from exceptions import ValidationError

class Patient:
    """Patient Model with Integrated Validation."""
    def __init__(self, patient_id, name, age, disease, contact):
        self.patient_id = str(patient_id).strip()
        self.name = str(name).strip()
        self.age = int(age)
        self.disease = str(disease).strip()
        self.contact = str(contact).strip()
        self.validate()

    def validate(self):
        """Feature 8: Validate Patient Data."""
        if not self.patient_id:
            raise ValidationError("Patient ID cannot be empty.")
        if not self.name or len(self.name) < 2:
            raise ValidationError("Name must be at least 2 characters long.")
        if self.age <= 0 or self.age > 120:
            raise ValidationError("Age must be between 1 and 120.")
        if not self.disease:
            raise ValidationError("Disease details cannot be empty.")
        if len(self.contact) != 10 or not self.contact.isdigit():
            raise ValidationError("Contact must be a valid 10-digit number.")

    def to_dict(self):
        return {
            "patient_id": self.patient_id,
            "name": self.name,
            "age": self.age,
            "disease": self.disease,
            "contact": self.contact
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["patient_id"],
            data["name"],
            data["age"],
            data["disease"],
            data["contact"]
        )

    def __str__(self):
        return f"ID: {self.patient_id} | Name: {self.name:<15} | Age: {self.age:<3} | Disease: {self.disease:<15} | Phone: {self.contact}"