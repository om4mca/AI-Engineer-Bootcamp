


def decorator_one(function):

    def wrapper(*args, **kwargs):

        print("Decorator One")

        return function(*args, **kwargs)

    return wrapper

def decorator_two(function):

    def wrapper(*args, **kwargs):

        print("Decorator Two")

        return function(*args, **kwargs)

    return wrapper

def decorator_two(function):

    def wrapper(*args, **kwargs):

        print("Decorator Two")

        return function(*args, **kwargs)

    return wrapper

@decorator_one
@decorator_two
def greet():
    print("Hello Om")