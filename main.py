
students = [
    {"name": "Rohit", "marks": [85, 90, 78]},
    {"name": "Rahul", "marks": [92, 88, 95]},
    {"name": "Rakesh", "marks": [65, 70, 72]},
]

print("STUDENT PERFORMANCE ANALYZER")
print("-" * 35)

for student in students:
    total = sum(student["marks"])
    average = total / len(student["marks"])

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"

    print(f"Name: {student['name']}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")
    print("-" * 35)
