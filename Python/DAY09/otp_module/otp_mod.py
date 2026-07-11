#--------------------------------------------
# AI Engineer Bootcamp
# Day 8
# Program: Random OTP Generator
# Author: Om Roy
# Date: 11-07-2026
#--------------------------------------------
import secrets
import string
from datetime import datetime, timedelta

class OTPManager:
    def __init__(self, validity_period_minutes: int = 2):
        """Initializes the manager with a specific expiration time frame."""
        self._active_otp = None
        self._expiration_time = None
        self.validity_period = validity_period_minutes

    def generate_numeric_otp(self, length: int = 6) -> str:
        """Generates a secure, digits-only OTP (e.g., 482915)."""
        # We draw secure choices directly from string digits '0123456789'
        otp = "".join(secrets.choice(string.digits) for _ in range(length))
        
        # Lock in values and set expiration window
        self._active_otp = otp
        self._expiration_time = datetime.now() + timedelta(minutes=self.validity_period)
        return otp

    def generate_alphanumeric_otp(self, length: int = 8) -> str:
        """Generates a secure, mixed case alphanumeric code (e.g., k7X2p9W1)."""
        pool = string.ascii_letters + string.digits
        otp = "".join(secrets.choice(pool) for _ in range(length))
        
        self._active_otp = otp
        self._expiration_time = datetime.now() + timedelta(minutes=self.validity_period)
        return otp

    def verify_otp(self, user_input: str) -> tuple[bool, str]:
        """
        Validates the provided OTP.
        Returns a tuple: (Is_Valid, Status_Message)
        """
        if not self._active_otp:
            return False, "Authentication Error: No active OTP session exists."
            
        # Check if the code has expired based on current time thresholds
        if datetime.now() > self._expiration_time:
            self.clear_otp()
            return False, "Verification Failed: The passcode has expired."
            
        # Constant-time comparison to prevent timing attacks
        if secrets.compare_digest(self._active_otp, user_input.strip()):
            self.clear_otp()  # Consume the token immediately upon success
            return True, "Success: Authentication successful."
            
        return False, "Verification Failed: Incorrect passcode entered."

    def clear_otp(self):
        """Invalidates the active token cache."""
        self._active_otp = None
        self._expiration_time = None