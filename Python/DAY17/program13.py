#--------------------------------------------
# AI Engineer Bootcamp
# Day 17
# Program: Hospital Patient Iterator
# Author: Om Roy
# Date: 22-07-2026
#--------------------------------------------

class PatientIterator:
    """Custom iterator class to traverse a collection of hospital patients one by one."""

    def __init__(self, patients):
        self.patients = patients
        self.index = 0

    def __iter__(self):
        # The iterator object must return itself from __iter__()
        return self

    def __next__(self):
        # Check if there are still patients left to iterate over
        if self.index < len(self.patients):
            patient = self.patients[self.index]
            self.index += 1
            return patient

        # Signal that the iteration has finished
        raise StopIteration


# --- Test Execution ---
if __name__ == "__main__":
    patients = [
        "Patient 101",
        "Patient 102",
        "Patient 103",
        "Patient 104",
        "Patient 105"
    ]

    patient_iterator = PatientIterator(patients)

    for patient in patient_iterator:
        print(patient)