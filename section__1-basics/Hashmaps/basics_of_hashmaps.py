# Nested dictionary example for practicing complex operations

students = {
    "Alice": {
        "age": 20,
        "courses": {
            "math": {"grade": "A", "credits": 3},
            "history": {"grade": "B+", "credits": 2}
        },
        "active": True
    },
    "Bob": {
        "age": 22,
        "courses": {
            "math": {"grade": "B", "credits": 3},
            "science": {"grade": "A-", "credits": 4}
        },
        "active": False
    },
    "Charlie": {
        "age": 21,
        "courses": {
            "history": {"grade": "A", "credits": 2},
            "science": {"grade": "B", "credits": 4}
        },
        "active": True
    }
}


for key, value in students.items():
    key = "Neeraj"
    print(key, value)

# Update the Student details:
del students["Alice"]
print(students)