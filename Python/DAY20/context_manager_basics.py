class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print(f"Opening {self.filename}...")
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing {self.filename}...")
        if self.file:
            self.file.close()
        # Returning True suppresses any raised exceptions (usually leave as None/False)

# Usage
with ManagedFile('example.txt') as f:
    f.write('Hello, world!')
# 'Closing example.txt...' is guaranteed to run here even if an error occurred inside