from functools import wraps


def log_operation(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        print(
            f"Operation started: "
            f"{function.__name__}"
        )

        result = function(*args, **kwargs)

        print(
            f"Operation completed: "
            f"{function.__name__}"
        )

        return result

    return wrapper

@log_operation
def add_patient(patient):
    print(f"Adding patient: {patient.name}")