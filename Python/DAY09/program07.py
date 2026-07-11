#--------------------------------------------
# AI Engineer Bootcamp
# Day 8
# Program: Current Time
# Author: Om Roy
# Date: 11-07-2026
#--------------------------------------------

from datetime import datetime

# 1. Fetch the exact current date and time
now = datetime.now()
print(f"Raw datetime object: {now}") 

# 2. Extract just the time elements
current_time_obj = now.time()
print(f"Raw time object:     {current_time_obj}")

# 3. Format it into clean strings
time_12hr = now.strftime("%I:%M:%S %p")  # 12-hour clock with AM/PM
time_24hr = now.strftime("%H:%M:%S")     # 24-hour military clock

print(f"12-Hour Format:      {time_12hr}")  # e.g., 05:13:27 PM
print(f"24-Hour Format:      {time_24hr}")  # e.g., 17:13:27

#end of the program