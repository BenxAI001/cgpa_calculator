"""CGPA calculator module with separable logic for testing.

Provides:
- grade_to_point(grade)
- calculate_cgpa(courses)
- an interactive CLI preserved under main()

This refactor separates calculation logic from input/output so it can be unit-tested.
"""
from typing import List, Tuple

GRADE_POINTS = {
    "A": 5.0,
    "B": 4.0,
    "C": 3.0,
    "D": 2.0,
    "E": 1.0,
    "F": 0.0,
}


def grade_to_point(grade: str) -> float:
    """Convert a letter grade (A-F) to grade points on a 5.0 scale.

    Raises ValueError for invalid grades.
    """
    if not isinstance(grade, str):
        raise ValueError("Grade must be a string.")
    g = grade.strip().upper()
    if g not in GRADE_POINTS:
        raise ValueError(f"Invalid grade: {grade}")
    return GRADE_POINTS[g]


def calculate_cgpa(courses: List[Tuple[float, str]]) -> float:
    """Calculate CGPA from an iterable of (credit_unit, grade) pairs.

    - credit_unit must be a positive float
    - grade must be a string representing A-F

    Returns the weighted average (grade points weighted by credit units).
    Raises ValueError for invalid input or zero total credits.
    """
    total_credit_units = 0.0
    total_grade_points = 0.0

    for credit_unit, grade in courses:
        try:
            credit = float(credit_unit)
        except Exception:
            raise ValueError("Credit unit must be a number.")
        if credit <= 0:
            raise ValueError("Credit units must be positive.")
        point = grade_to_point(grade)
        total_credit_units += credit
        total_grade_points += point * credit

    if total_credit_units == 0:
        raise ValueError("Total credit units is zero.")

    return total_grade_points / total_credit_units


def _prompt_positive_float(prompt: str) -> float:
    while True:
        try:
            val = float(input(prompt))
            if val <= 0:
                print("Please enter a value greater than zero.")
                continue
            return val
        except ValueError:
            print("❌ Invalid input! Please enter a numeric value.")


def _prompt_grade(prompt: str) -> str:
    while True:
        g = input(prompt).strip().upper()
        if g in GRADE_POINTS:
            return g
        print("Invalid grade — enter one of A, B, C, D, E, F.")


def interactive_main() -> None:
    print("===== CGPA CALCULATOR =====")

    while True:
        try:
            n = int(input("Enter number of courses: "))
            if n <= 0:
                print("Enter a positive number of courses.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer for the number of courses.")

    courses = []  # list of (credit_unit, grade)

    for i in range(1, n + 1):
        print(f"\nCourse {i}:")
        course_name = input("Course name (optional): ")
        credit = _prompt_positive_float("Credit unit: ")
        grade = _prompt_grade("Grade (A-F): ")
        courses.append((credit, grade))

    try:
        cgpa = calculate_cgpa(courses)
    except ValueError as e:
        print(f"Error calculating CGPA: {e}")
        return

    print("\n==========================")
    print(f"Your CGPA is: {cgpa:.2f}")
    print("==========================")


def main() -> None:
    interactive_main()


if __name__ == "__main__":
    main()
