#--------------------------------------------
# AI Engineer Bootcamp
# Day 19
# Program: Authentication Decorator
# Author: Om Roy
# Date: 24-07-2026
#--------------------------------------------

from functools import wraps

# Simulated active session store or token state
SESSION_STORE = {
    "auth_token": "valid_token_xyz123",
    "user_id": 402,
    "username": "om_prakash"
}


def require_auth(func):
    """Decorator to enforce user authentication before executing a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = kwargs.get("token") or SESSION_STORE.get("auth_token")
        
        # 1. Check if token exists
        if not token:
            print("🔒 [401 Unauthorized]: No authentication token provided.")
            return {"status": 401, "message": "Authentication token missing."}
            
        # 2. Validate token against active sessions
        if token != SESSION_STORE.get("auth_token"):
            print("❌ [403 Forbidden]: Invalid or expired token.")
            return {"status": 403, "message": "Invalid authentication token."}
            
        print(f"🔑 Authentication verified for user '{SESSION_STORE['username']}'.")
        return func(*args, **kwargs)
        
    return wrapper


# --- Example Usage ---

@require_auth
def get_user_profile():
    return {
        "user_id": SESSION_STORE["user_id"],
        "username": SESSION_STORE["username"],
        "email": "om@example.com"
    }


# --- Execution Tests ---

print("=== Test 1: Valid Session Authentication ===")
profile = get_user_profile()
print(f"Response: {profile}\n")


print("=== Test 2: Passing Invalid Token ===")
profile_invalid = get_user_profile(token="wrong_token_999")
print(f"Response: {profile_invalid}\n")


print("=== Test 3: No Token / Unauthenticated ===")
SESSION_STORE["auth_token"] = None  # Simulating logged-out user
profile_none = get_user_profile()
print(f"Response: {profile_none}")