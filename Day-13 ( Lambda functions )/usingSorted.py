students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78)
]

students_sorted = sorted(students, key=lambda student: student[1])

print(students_sorted)