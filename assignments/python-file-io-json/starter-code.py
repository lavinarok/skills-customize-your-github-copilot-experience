import json

# Sample data for a small JSON-based program
students = [
    {"name": "Ava", "grade": "A"},
    {"name": "Leo", "grade": "B"},
]

# Save to a file
with open("students.json", "w") as file:
    json.dump(students, file)

# Load from the file
with open("students.json", "r") as file:
    loaded_students = json.load(file)

print("Saved students:", loaded_students)
