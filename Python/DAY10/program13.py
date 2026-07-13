#--------------------------------------------
# AI Engineer Bootcamp
# Day 10
# Program: Student Marks Validation
# Author: Om Roy
# Date: 13-07-2026
#--------------------------------------------

class InvalidMarkError(Exception):
    """Raised when a grade value falls outside the logical academic limits (0-100)."""
    pass


class ReportCardSystem:
    @staticmethod
    def process_marks(marks_dict):
        validated_marks = {}
        total_possible = len(marks_dict) * 100
        
        for subject, score_raw in marks_dict.items():
            # 1. Check for numeric type conversion
            try:
                score = float(score_raw)
            except ValueError:
                raise ValueError(f"Formatting Error: The score for '{subject}' must be a clear number.")
            
            # 2. Check academic boundary conditions
            if score < 0 or score > 100:
                raise InvalidMarkError(f"Bound Violation: '{subject}' received a score of {score}. Marks must be between 0 and 100.")
                
            validated_marks[subject] = score

        # 3. Compile processing stats
        total_earned = sum(validated_marks.values())
        percentage = (total_earned / total_possible) * 100 if total_possible > 0 else 0
        
        return {
            "Scores": validated_marks,
            "Total": total_earned,
            "Max_Possible": total_possible,
            "Percentage": percentage
        }


def main():
    print("=== Academic Marks Validation Gateway ===")
    subjects = ["Mathematics", "Science", "History"]
    
    while True:
        print(f"\nPlease enter scores out of 100 for: {', '.join(subjects)}")
        print("(Type 'exit' to shut down processing module)")
        
        # Collect values dynamically
        raw_inputs = {}
        exit_flag = False
        
        for sub in subjects:
            user_entry = input(f" -> {sub}: ").strip()
            if user_entry.lower() == 'exit':
                exit_flag = True
                break
            raw_inputs[sub] = user_entry
            
        if exit_flag:
            break

        try:
            # Pass dictionary to processing validation gateway
            report = ReportCardSystem.process_marks(raw_inputs)
            
        except ValueError as e:
            print(f"\n[Data Entry Error]: {e}")
            
        except InvalidMarkError as e:
            print(f"\n[Academic Policy Error]: {e}")
            
        else:
            # Executed only if entire batch of subjects clears perfectly
            print(f"\n📊 === Academic Report Card Generated ===")
            for subject, final_score in report["Scores"].items():
                print(f" * {subject:<12}: {final_score:>6.2f} / 100")
            print("-" * 41)
            print(f" Final Ledger : {report['Total']:.1f} / {report['Max_Possible']}")
            print(f" Percentage   : {report['Percentage']:.2f}%")
            
        finally:
            print("\n" + "="*45)

    print("\nSession safely closed. All verified academic records written to permanent registry.")


if __name__ == "__main__":
    main()


# end of the program     