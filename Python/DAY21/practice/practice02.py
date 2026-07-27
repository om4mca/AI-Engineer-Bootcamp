
#--------------------------------------------
# AI Engineer Bootcamp
# Day 21
# Program: Dictionary + Function
# Author: Om Roy
# Date: 27-07-2026
#--------------------------------------------

def print_user_profile(user):
    # Access dictionary key-value pairs
    print(f"User: {user.get('name', 'Guest')}")
    print(f"Role: {user.get('role', 'User')}")

profile = {"name": "Om", "role": "Admin", "id": 104}
print_user_profile(profile)