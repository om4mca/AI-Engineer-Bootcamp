#--------------------------------------------
# AI Engineer Bootcamp
# Day 19
# Program: Permission Decorator
# Author: Om Roy
# Date: 24-07-2026
#--------------------------------------------


from functools import wraps

# Simulated current logged-in user session
CURRENT_USER = {
    "username": "om_prakash",
    "role": "Editor"  # Try changing to "Admin", "Editor", or "Guest"
}


def require_role(*allowed_roles):
    """Decorator factory that checks if current user has an authorized role."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_role = CURRENT_USER.get("role")
            
            # Check authorization
            if user_role not in allowed_roles:
                raise PermissionError(
                    f"⛔ Access Denied for '{CURRENT_USER['username']}'! "
                    f"Role '{user_role}' is not in allowed roles: {allowed_roles}"
                )
            
            print(f"✅ Authorization Granted for '{CURRENT_USER['username']}' ({user_role}).")
            return func(*args, **kwargs)
            
        return wrapper
    return decorator


# --- Example Usage ---

@require_role("Admin")
def delete_database():
    return "💥 Database deleted!"


@require_role("Admin", "Editor")
def publish_article(title):
    return f"📰 Article '{title}' published successfully."


# --- Execution Tests ---

print("=== Test 1: Publish Article ===")
try:
    status = publish_article("Python Decorators Guide")
    print(status)
except PermissionError as err:
    print(err)


print("\n=== Test 2: Delete Database ===")
try:
    status = delete_database()
    print(status)
except PermissionError as err:
    print(err)