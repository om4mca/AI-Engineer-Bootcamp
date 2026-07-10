#--------------------------------------------
# AI Engineer Bootcamp
# Day 8
# Program: Greeting Function
# Author: Om Roy
# Date: 10-07-2026
#--------------------------------------------

from datetime import datetime

def get_greeting(name, role="User"):
    """Generates a time-based personalized greeting message."""
    # Get the current hour of the day (0-23)
    current_hour = datetime.now().hour
    
    # Determine time-of-day phrase
    if current_hour < 12:
        time_phrase = "Good morning"
    elif current_hour < 18:
        time_phrase = "Good afternoon"
    else:
        time_phrase = "Good evening"
        
    # Build custom message based on system access level
    if role.lower() == "admin":
        role_note = " [System Administrator Access Enabled]"
    else:
        role_note = ""
        
    return f"{time_phrase}, {name}!{role_note} Welcome back."

# --- Example Usage ---
# Regular User
print(get_greeting("Om")) 
# Output changes dynamically based on your clock: e.g., "Good afternoon, Om! Welcome back."

# Admin User
print(get_greeting("Sudhir", role="Admin"))
# Output: "Good afternoon, Sarah! [System Administrator Access Enabled] Welcome back."

# end of the program