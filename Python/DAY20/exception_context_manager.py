class MyContextManager:

    def __enter__(self):
        print("Context Started")
        return self

    def __exit__(self, exc_type, exc_value, traceback):

        print("Context Ending")

        if exc_type:
            print("Exception occurred")

        return False
    
with MyContextManager():

    print("Inside Context")

    raise ValueError("Something went wrong")