#--------------------------------------------
# AI Engineer Bootcamp
# Day 19
# Program: **kwargs Decorator
# Author: Om Roy
# Date: 24-07-2026
#--------------------------------------------

from functools import wraps

def kwargs_only_decorator(func):
    @wraps(func)
    def wrapper(**kwargs):
        # 1. Action before calling the target function
        print(f"Captured {len(kwargs)} keyword argument(s): {kwargs}")
        
        # 2. Pass keyword arguments to the original function
        result = func(**kwargs)
        
        # 3. Action after calling the target function
        print("Execution completed.")
        return result
        
    return wrapper


# --- Example Usage ---

@kwargs_only_decorator
def create_profile(username, role, status="Active"):
    return {"user": username, "role": role, "status": status}


# --- Execution ---

# Must be called strictly using keyword arguments (key=value)
profile = create_profile(username="om_prakash", role="Admin", status="Verified")
print(f"Result: {profile}")