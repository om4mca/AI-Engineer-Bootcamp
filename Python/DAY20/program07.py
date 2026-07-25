import os
from contextlib import suppress

# Silently ignore FileNotFoundError if the file doesn't exist
with suppress(FileNotFoundError):
    os.remove("temporary_file.txt")

print("Execution continues cleanly even if the file was missing!")