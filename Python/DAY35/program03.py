import statistics

# Handles unimodal and multimodal data
data = [10, 15, 20, 25, 30, 30, 45, 45, 45]

# Single mode (most frequent)
mode_val = statistics.mode(data) 
print(f"Primary Mode: {mode_val}") # Output: 45

# All modes (in case of ties / bimodal)
multimodes = statistics.multimode(data)
print(f"All Modes   : {multimodes}") # Output: [45]