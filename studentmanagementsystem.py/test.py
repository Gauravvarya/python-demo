file_name = "student.json" # file name to store student data
import json
def load_data():
    try:
        with open(file_name, "r") as f:
            data = json.load(f)
            return data
    except:
            return []
    
def save_data(data):
        with open (file_name,"w") as f:
            json.dump(data,f)
    

# Data store in dictionary.
students = []
student = {
    "name": "",
    "roll_no": "",
    "marks": 0
}

# Function to add a student to the list of students.
def add_student():
    name = input("Enter student name:")
    roll_no = input("Enter student roll number:")
    marks = int(input("Enter student marks:"))
    student["name"] = name
    student["roll_no"] = roll_no
    student["marks"] = marks

    students.append(student)
    print("Student added successfully!")
    save_data(students)

# Function to display all students.
def display_students():
    students = load_data()
    if (len(students) == 0):
        print("No students found.")
    else:
        print("List of students:")
        for student in students:
            print(f"name:{student['name']}, roll_no:{student['roll_no']}, marks:{student['marks']}")

# search student by roll number
def search_student():
    students
    roll_no =input("Enter student roll number to search:")
    for student in students:
        if student['roll_no'] == roll_no:
            print("Student found:")
            print(f"name:{student['name']}, roll_no:{student['roll_no']}, marks:{student['marks']}")
        else:
            print("Student not found.")

#menu for user to choose options
def menu():
    while True:
        print("1. Add student")
        print("2. Display students")
        print("3. Search student by roll number")
        print("4. Exit")
        choice = input("Enter your choice:")
        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
        if __name__ == "__main__":
            menu()