# Define a class to represent a student
class Student:
    def __init__(self, name, student_id, grade1, grade2):
        self.name = name
        self.student_id = student_id
        self.grade1 = grade1
        self.grade2 = grade2

    # Method to display student details
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Grade 1: {self.grade1}")
        print(f"Grade 2: {self.grade2}")
        print()

# List to store all students
students = []

# Function to add a new student
def add_student():
    name = input("Enter the student's name: ")
    student_id = int(input("Enter the student's ID: "))
    grade1 = float(input("Enter grade 1: "))
    grade2 = float(input("Enter grade 2: "))
    student = Student(name, student_id, grade1, grade2)
    students.append(student)
    print(f"Student {name} added successfully!\n")

# Function to display all students
def display_students():
    if not students:
        print("No students registered yet.\n")
    else:
        print("List of students:")
        for student in students:
            student.display_details()

# Function to find a student by ID
def find_student():
    student_id = int(input("Enter the student's ID to search: "))
    for student in students:
        if student.student_id == student_id:
            print("Student found:")
            student.display_details()
            return
    print(f"No student found with ID {student_id}.\n")

# Function to remove a student by ID
def remove_student():
    student_id = int(input("Enter the student's ID to remove: "))
    for student in students:
        if student.student_id == student_id:
            students.remove(student)
            print(f"Student with ID {student_id} removed.\n")
            return
    print(f"No student found with ID {student_id}.\n")

# Function to update a student's ID
def update_student():
    student_id = int(input("Enter the current student ID: "))
    new_id = int(input("Enter the new student ID: "))
    for student in students:
        if student.student_id == student_id:
            student.student_id = new_id
            print(f"Student ID updated to {new_id}.\n")
            return
    print(f"No student found with ID {student_id}.\n")
 
# Main menu function
def menu():
    print("\nWelcome to Student Management System")
    print("1. Add a student")
    print("2. Display all students")
    print("3. Find a student")
    print("4. Remove a student")
    print("5. Update a student's ID")
    print("6. Exit")

# Main program loop
while True:
    menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        find_student()
    elif choice == '4':
        remove_student()
    elif choice == '5':
        update_student()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")