n = int(input("Enter number of students: "))

students = []
subjects = ["maths", "science", "social"]

for _ in range(n):
    name = input("Enter name of student: ")
    students.append(name)

for student in students:
    total_marks = 0
    print(f"\nEnter marks for {student}:")
    for subject in subjects:
        while True:
            try:
                mark = int(input(f"  {subject}: "))
                if 0 <= mark <= 100:
                    break
                else:
                    print("  Please enter marks between 0 and 100.")
            except ValueError:
                print("  Invalid input. Please enter a number.")
        total_marks += mark

    avg = total_marks / len(subjects)

    # Decide grade and pass/fail per student
    if avg >= 90:
        grade = "Class 1 (90% and above)"
        status = "Passed"
    elif avg >= 70:
        grade = "Class 2 (70% to 89%)"
        status = "Passed"
    elif avg >= 50:
        grade = "Class 3 (50% to 69%)"
        status = "Passed"
    else:
        grade = "Fail (Below 50%)"
        status = "Failed"

    print(f"{student}'s average: {avg:.2f} - {grade} - {status}")

       