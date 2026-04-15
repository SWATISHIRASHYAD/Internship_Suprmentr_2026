# *Assignment (19/02/2026)*

# *Assignment Name* : Student Data Manager
# *Description* : Store data for 5 students using dictionaries, print topper, class average, and assign grades.

# Student Data Manager

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

def main():
    students = {}

    # Input for 5 students
    for i in range(1, 6):
        print(f"\nEnter details for Student {i}")
        name = input("Name: ")
        marks = float(input("Marks: "))
        students[name] = marks

    # Calculate total and average
    total_marks = sum(students.values())
    average = total_marks / len(students)

    # Find topper
    topper = max(students, key=students.get)

    print("\n--- Student Results ---")
    for name, marks in students.items():
        grade = calculate_grade(marks)
        print(f"{name} - Marks: {marks}, Grade: {grade}")

    print("\n--- Summary ---")
    print(f"Topper: {topper} ({students[topper]} marks)")
    print(f"Class Average: {average:.2f}")

if __name__ == "__main__":
    main()


