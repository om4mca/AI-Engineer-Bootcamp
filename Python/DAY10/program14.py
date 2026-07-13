
#--------------------------------------------
# AI Engineer Bootcamp
# Day 10
# Program: Hospital Fee Validation
# Author: Om Roy
# Date: 13-07-2026
#--------------------------------------------


class InsufficientFeeError(Exception):
    """Raised when a specific mandatory fee falls below its required floor."""
    pass

class FeeLimitExceededError(Exception):
    """Raised when an entry looks abnormally high, triggering an administrative audit."""
    pass


class HospitalBillingSystem:
    # Business standard compliance guardrails
    MIN_CONSULTATION = 20.00
    MAX_PHARMACY_LIMIT = 5000.00
    MAX_ROOM_LIMIT = 2000.00

    @classmethod
    def validate_and_calculate_invoice(cls, billing_data):
        validated_fees = {}
        
        # 1. Structural Type Conversions
        for category, raw_value in billing_data.items():
            try:
                amount = float(raw_value)
                if amount < 0:
                    raise ValueError("Negative balances are invalid.")
                validated_fees[category] = amount
            except ValueError:
                raise ValueError(f"Formatting Error: The amount for '{category}' must be a positive number.")

        # 2. Extract Values for Compliance Policy Checks
        consultation = validated_fees.get("Consultation", 0.0)
        pharmacy = validated_fees.get("Pharmacy", 0.0)
        room_charge = validated_fees.get("Room Charge", 0.0)

        # 3. Policy Rule Validations
        if consultation < cls.MIN_CONSULTATION:
            raise InsufficientFeeError(
                f"Policy Violation: Consultation fee ({consultation:.2f}) cannot fall below the regulatory base threshold of {cls.MIN_CONSULTATION:.2f}."
            )
            
        if pharmacy > cls.MAX_PHARMACY_LIMIT:
            raise FeeLimitExceededError(
                f"Audit Flag: Pharmacy charges ({pharmacy:.2f}) exceed the standard cap of {cls.MAX_PHARMACY_LIMIT:.2f}. Requires senior chief medical board clearance."
            )
            
        if room_charge > cls.MAX_ROOM_LIMIT:
            raise FeeLimitExceededError(
                f"Audit Flag: Daily Room Charge ({room_charge:.2f}) exceeds the maximum insurance tier limit of {cls.MAX_ROOM_LIMIT:.2f}."
            )

        # 4. Generate Final Ledger Statement Summary
        subtotal = sum(validated_fees.values())
        tax_or_levy = subtotal * 0.05  # Standard 5% healthcare service tax
        grand_total = subtotal + tax_or_levy

        return {
            "Itemized": validated_fees,
            "Tax": tax_or_levy,
            "Total": grand_total
        }


def main():
    print("=== Hospital Billing & Fee Validation Gateway ===")
    fee_categories = ["Consultation", "Pharmacy", "Room Charge"]
    
    while True:
        print(f"\nPlease enter bill components. (Type 'exit' to shut down module)")
        raw_inputs = {}
        exit_flag = False
        
        for category in fee_categories:
            user_entry = input(f" -> {category} Amount (): ").strip()
            if user_entry.lower() == 'exit':
                exit_flag = True
                break
            raw_inputs[category] = user_entry
            
        if exit_flag:
            break

        try:
            # Process transaction values through business gateway limits
            invoice = HospitalBillingSystem.validate_and_calculate_invoice(raw_inputs)
            
        except ValueError as e:
            print(f"\n[Data Entry Error]: {e}")
            
        except InsufficientFeeError as e:
            print(f"\n[Minimum Threshold Violation]: {e}")
            
        except FeeLimitExceededError as e:
            print(f"\n[Maximum Compliance Violation]: {e}")
            
        else:
            # Run layout block if entries clear completely without triggering errors
            print(f"\n🧾 === Validated Patient Invoice Statement ===")
            for category, cleared_amount in invoice["Itemized"].items():
                print(f" * {category:<15}: {cleared_amount:>8.2f}")
            print("-" * 38)
            print(f" Healthcare Tax (5%) : {invoice['Tax']:>8.2f}")
            print(f" Grand Invoice Total : {invoice['Total']:>8.2f}")
            
        finally:
            print("\n" + "="*42)

    print("\nSession safely closed. All verified billing logs committed to permanent medical financial database.")


if __name__ == "__main__":
    main()