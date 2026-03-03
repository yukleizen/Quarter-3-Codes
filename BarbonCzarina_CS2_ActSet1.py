# Create an empty dictionary
student = {}

# Collect input from the user
student["name"] = input("Enter your name: ")
student["age"] = input("Enter your age: ")
student["subject"] = input("Enter your favorite subject: ")

# Print the student's information in a clear format
print("\nStudent Information:")
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Favorite Subject: {student['subject']}")
