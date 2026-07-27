from contextlib import contextmanager


@contextmanager
def open_file(filename, mode):

    file = open(filename, mode)

    try:
        yield file

    finally:
        file.close()

with open_file(
    "data/patients.txt",
    "a"
) as file:

    file.write("Patient Record\n")        


from managers.file_manager import open_file


def save_patient(patient):

    with open_file(
        "data/patients.txt",
        "a"
    ) as file:

        file.write(
            f"{patient.patient_id},"
            f"{patient.name},"
            f"{patient.age},"
            f"{patient.disease}\n"
        )    