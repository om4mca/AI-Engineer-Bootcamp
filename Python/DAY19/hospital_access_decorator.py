

#--------------------------------------------
# AI Engineer Bootcamp
# Day 19
# Program: Hospital Access Logging Decorator
# Author: Om Roy
# Date: 24-07-2026
#--------------------------------------------



import time
from functools import wraps

# 1. Logging Decorator
def log_access(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("\n[LOG] User accessed hospital system")
        result = func(*args, **kwargs)
        print("[LOG] Access completed")
        return result
    return wrapper

# 2. Permission Check Decorator
def check_permission(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Simulating a permission check
        is_authorized = True  
        if is_authorized:
            print("[SECURITY] Permission Granted: Admin/Doctor level access.")
            return func(*args, **kwargs)
        else:
            print("[SECURITY] Access Denied: Insufficient permissions!")
            return None
    return wrapper

# 3. Execution Timer Decorator
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[TIMER] Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper


# --- Basic Usage ---

@log_access
def view_patient_records():
    print("Displaying Patient Records")

print("=== Basic Single Decorator Execution ===")
view_patient_records()


# --- Upgrade: Multiple Decorators Chaining ---

@log_access
@check_permission
@timer
def view_sensitive_patient_data(patient_id):
    print(f"Displaying High-Security Data for Patient ID: {patient_id}")

print("\n=== Upgraded: Multiple Decorators Execution ===")
view_sensitive_patient_data(101)