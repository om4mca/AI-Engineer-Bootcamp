from services.patient_service import PatientService
from managers.file_manager import open_file


def main():

    service = PatientService()

    try:

        patient = service.add_patient(
            101,
            "Om",
            42,
            "Fever"
        )

        print(patient)

        with open_file(
            "data/patients.txt",
            "a"
        ) as file:

            file.write(
                f"{patient}\n"
            )

    except Exception as error:

        print(
            f"Error: {error}"
        )


if __name__ == "__main__":
    main()