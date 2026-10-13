students = {
    "Amit": {"marks": 85},
    "Neha": {"marks": 92}
}

print(students["Amit"]["marks"])
print(max(students, key=lambda x: students[x]["marks"]))