# CGPA Calculator

def calculate_cgpa():
    print("===== CGPA CALCULATOR =====")
    
    total_credit_units = 0
    total_grade_points = 0
    
    try:
        n = int(input("Enter number of courses: "))
    except ValueError:
        print("Please enter a valid number for the courses.")
        return
    
    for i in range(1, n + 1):
        print(f"\nCourse {i}:")
        course_name = input("Course name: ")
        
                # Credit unit input with error handling
      
        while True:
            try:
                credit_unit = float(input("Credit unit: "))
                break  # Exit the loop if conversion is successful
            except ValueError:
                print("❌ Invalid input! Please enter a numeric value for credit units.")
        
        while True:
        	grade = input("Grade (A-F): ").upper()
        	if grade not in ["A","B","C","D","E","F"]:
        		print("Invalid Grade❌❌")
        	else:
        		break
        
        # Grade to point conversion
        if grade == 'A':
            grade_point = 5.0
        elif grade == 'B':
            grade_point = 4.0
        elif grade == 'C':
            grade_point = 3.0
        elif grade == 'D':
            grade_point = 2.0
        elif grade == 'E':
            grade_point = 1.0
        elif grade == 'F':
            grade_point = 0.0
        else:
            print("❌ Invalid grade! Try again.")
            continue
        
        total_credit_units += credit_unit
        total_grade_points += grade_point * credit_unit
    
    if total_credit_units == 0:
        print("No valid courses entered.")
    else:
        cgpa = total_grade_points / total_credit_units
        print("\n==========================")
        print(f"Your CGPA is: {cgpa:.2f}")
        print("==========================")

# Run the calculator
calculate_cgpa()
