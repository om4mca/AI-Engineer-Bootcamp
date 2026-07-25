class MyContextManager:

    def __enter__(self):
        print("Entering Context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting Context")


with MyContextManager():
    print("Inside Context Manager")