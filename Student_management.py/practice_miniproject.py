students = []

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

class Menu:
    def add_students(self):
        while len(students) < 10:
            name = input("Enter the student name: ")
            roll_no = int(input("Enter the Roll no: "))
            marks = float(input("Enter the marks: "))
            s = Student(name, roll_no, marks)
            students.append(s)
            print("Student added successfully")
            if len(students) == 10:
                print("Student limit is reached")
                break
            a = input("Want to enter more students (yes/no): ").strip().lower()
            if a != "yes":
                break

    def view_students(self):
        if not students:
            print("No students to display.")
        else:
            for s in students:
                print(f"Name: {s.name}, Roll No: {s.roll_no}, Marks: {s.marks}")

    def search_students(self):
        if not students:
            print("Student not found")
            return 
        search_roll = int(input("Enter the Roll no to search: "))
        found = False
        for s in students:
            if s.roll_no == search_roll:
                print(f"Name: {s.name}, Marks: {s.marks}")
                found = True
                break
        if not found:
            print("Student not found")

    def update_name(self):
        roll = int(input("Enter the Roll no to update: "))  
        found = False
        for i in students:
            if i.roll_no == roll:
                new_name = input("Enter the new name: ")
                new_marks= input("Enter the marks:")
                i.name = new_name
                i.marks = new_marks
                print("Name and marks are updated ")
                found = True
                break
        if not found:
            print("Student not found")


s1 = Menu()
s1.add_students()
s1.search_students()
s1.update_name()
s1.view_students()  


