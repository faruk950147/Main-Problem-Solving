students = []  # In-memory list to store student data

# CREATE
def create_student(name, age, department):
    student_id = len(students) + 1
    student = {'id': student_id, 'name': name, 'age': age, 'department': department}
    students.append(student)
    print("Student added successfully.")

# READ
def read_students():
    if not students:
        print("No student found.")
    for student in students:
        print(student)

# UPDATE
def update_student(student_id, name, age, department):
    for student in students:
        if student['id'] == student_id:
            student['name'] = name
            student['age'] = age
            student['department'] = department
            print("Student updated successfully.")
            return
    print("Student not found.")

# DELETE
def delete_student(student_id):
    global students
    students = [student for student in students if student['id'] != student_id]
    print("Student deleted successfully.")

# MENU
def menu():
    while True:
        print("\n=== Student CRUD App (No DB) ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Name: ")
            age = int(input("Age: "))
            department = input("Department: ")
            create_student(name, age, department)

        elif choice == '2':
            read_students()

        elif choice == '3':
            student_id = int(input("Enter Student ID to update: "))
            name = input("New Name: ")
            age = int(input("New Age: "))
            department = input("New Department: ")
            update_student(student_id, name, age, department)

        elif choice == '4':
            student_id = int(input("Enter Student ID to delete: "))
            delete_student(student_id)

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")

menu()