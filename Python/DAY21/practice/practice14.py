#--------------------------------------------
# AI Engineer Bootcamp
# Day 21
# Program: Generator + File Processing
# Author: Om Roy
# Date: 27-07-2026
#--------------------------------------------

# Stream lines without loading the whole file into memory
def stream_clean_lines(filepath):
    with open(filepath, "r") as file:
        for line in file:  # Yields 1 line at a time
            cleaned = line.strip()
            if cleaned and not cleaned.startswith("#"):  # Skip blank lines & comments
                yield cleaned

# Process lines as they arrive
for line in stream_clean_lines("config.log"):
    print(f"Processing: {line}")