import time
from otp_mod import OTPManager


def main():
    print("=== Core Multi-Factor Authentication Engine ===")
    auth_gate = OTPManager(validity_period_minutes=2)
    
    # 1. Trigger numeric verification token dispatch (e.g., mobile SMS pipeline)
    print("\n[Action] Triggering 6-Digit SMS Token...")
    sms_code = auth_gate.generate_numeric_otp(length=6)
    print(f"-> [SIMULATED SMS OUTBOX] Your verification code is: {sms_code}")
    
    # 2. Simulate user matching verification success
    print("\n--- Scenario A: User inputs the correct code immediately ---")
    user_attempt = sms_code
    success, message = auth_gate.verify_otp(user_attempt)
    print(f"User Input: {user_attempt}")
    print(f"Result:     {message}")
    
    # 3. Trigger alpha-numeric verification token dispatch (e.g., Secure Email Portal)
    print("\n[Action] Triggering Alphanumeric Session Token...")
    email_code = auth_gate.generate_alphanumeric_otp(length=8)
    print(f"-> [SIMULATED EMAIL OUTBOX] Secure Login Token: {email_code}")
    
    # 4. Simulate user typing an incorrect value
    print("\n--- Scenario B: User makes a typing error ---")
    bad_attempt = "WRONG123"
    success, message = auth_gate.verify_otp(bad_attempt)
    print(f"User Input: {bad_attempt}")
    print(f"Result:     {message}")

if __name__ == "__main__":
    main()