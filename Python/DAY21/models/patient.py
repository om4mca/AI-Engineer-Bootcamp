class Patient:

    def __init__(self, patient_id, name, age, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease

    def display_info(self):
        return (
            f"ID: {self.patient_id}, "
            f"Name: {self.name}, "
            f"Age: {self.age}, "
            f"Disease: {self.disease}"
        )

    def __str__(self):
        return self.display_info()