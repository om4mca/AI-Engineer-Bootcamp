#--------------------------------------------
# AI Engineer Bootcamp
# Day 10
# Program: Patient Registration
# Author: Om Roy
# Date: 13-07-2026
#--------------------------------------------

import re

class InvalidAgeError(Exception):
    """Raised when an age value falls outside logical biological ranges."""
    pass

class InvalidContactError(Exception):
    """Raised when a phone number does not conform to dialing code standards."""
    pass

class FeeStructureError(Exception):
    """Raised when a consultation fee layout breaks financial logic."""
    pass


class PatientRecordGateway:
    @staticmethod
    def validate_and_create(name_raw, age_raw, phone_raw, fee_raw):
        # 1. Name Parsing & Basic Structural Inspection
        name = str(name_raw).strip()
        if not name:
            raise ValueError("Data Input Failure: Patient Name field cannot be left blank.")
        if not re.match(r"^[A-Za-z\s\-\.]+$", name):
            raise ValueError("Data Input Failure: Patient Name must contain alphabetic characters only.")

        # 2. Age Range & Integrity Checks
        try:
            age = int(age_raw)
        except ValueError:
            raise ValueError("Parsing Error: Patient Age must be a valid whole integer number.")
            
        if age <= 0:
            raise InvalidAgeError("Age Validation Error: Age metrics must be a strictly positive number.")
        if age > 125:
            raise InvalidAgeError(f"Age Validation Error: Inputted age ({age}) exceeds logical maximum human biological limits.")

        # 3. Contact Detail Verification
        phone = str(phone_raw).strip().replace(" ", "").replace("-", "")
        if not phone.isdigit() or len(phone) != 10:
            raise InvalidContactError(
                f"Contact Validation Error: '{phone_raw}' is structurally invalid. "
                f"Mobile numbers must contain exactly 10 digits."
            )

        # 4. Fee Valuation Handling
        try:
            fee = float(fee_raw)
        except ValueError:
            raise ValueError("Parsing Error: Consultation Fee must be a clear decimal amount.")
            
        if fee < 0:
            raise FeeStructureError("Financial Policy Error: Base consultation fees cannot be negative.")
        if fee > 10000.00:
            raise FeeStructureError(
                f"Financial Policy Error: Fee ({fee:,.2f}) triggers administrative limits. "
                f"Amounts greater than 10,000.00 require board clearance overrides."
            )

        # Build clean validated system payload array
        return {
            "name": name.title(),
            "age": age,
            "phone": f"({phone[:3]}) {phone[3:6]}-{phone[6:]}", # Clear phone readout structure
            "fee": fee
        }


def main():
    print("=== Secure Hospital Admissions Intake Gateway ===")
    print("Initialize intake profile sequence. Type 'quit' at the name prompt to exit.\n")
    
    registry_database = []

    while True:
        name_input = input("Enter Patient Full Name: ").strip()
        if name_input.lower() == 'quit':
            break
            
        age_input = input("Enter Patient Age: ").strip()
        phone_input = input("Enter 10-Digit Mobile Number: ").strip()
        fee_input = input("Enter Base Consultation Fee : ").strip()

        try:
            # Route individual strings through the validation check engine
            cleared_profile = PatientRecordGateway.validate_and_create(
                name_input, age_input, phone_input, fee_input
            )
            
        except ValueError as e:
            print(f"\n🚨 [Formatting Type Error]: {e}")
            
        except InvalidAgeError as e:
            print(f"\n🚨 [Biological Scope Violation]: {e}")
            
        except InvalidContactError as e:
            print(f"\n🚨 [Telephony Compliance Fault]: {e}")
            
        except FeeStructureError as e:
            print(f"\n🚨 [Billing Matrix Exception]: {e}")
            
        else:
            # Executes strictly if the data payload checks pass with zero triggers
            registry_database.append(cleared_profile)
            print(f"\n✅ [Admission Profile Confirmed Successfully]")
            print(f" -> Name Registered : {cleared_profile['name']}")
            print(f" -> Metric Age Room : {cleared_profile['age']} Years Old")
            print(f" -> Formatted Cell  : {cleared_profile['phone']}")
            print(f" -> Intake Fee Paid : {cleared_profile['fee']:,.2f}")
            
        finally:
            print(f"\nTotal Registered Profiles Active in Memory Cache: {len(registry_database)}")
            print("-" * 65 + "\n")

    print("Session disconnected safely. All validated records committed securely to local registry memory.")


if __name__ == "__main__":
    main()


# end of the program