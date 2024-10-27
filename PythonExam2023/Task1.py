# Task 1

class Person:  # Parent class "Person"
    def __init__(self, fname, lname, age):  # Attributes
        self.fname = fname
        self.lname = lname
        self.age = age
        
    def get_info(self):  # Method for printing Person attributes
        print("Full name:", self.fname, self.lname)
        print("Age:", self.age)
        
class Student(Person):  # Child class, inheriting Person class
    def __init__(self, fname, lname, age, student_id):  # Attributes
        super().__init__(fname, lname, age)  # super() for inheriting Person attributes
        self.student_id = student_id
        
    def get_stuinfo(self):  # Method for printing student info
        Person.get_info(self)  # Inheriting Person get_info method
        print("Student id:", self.student_id)
        
class Employee(Person):  # Child class, inheriting Person class
    def __init__(self, fname, lname, age, employee_number, salary):  # Attributes
        super().__init__(fname, lname, age)  # super() for inheriting Person attributes
        self.employee_number = employee_number
        self.salary = salary
        
    def get_empinfo(self):  # Method for printing employee info
        Person.get_info(self)  # Inheriting Person get_info method
        print("Employee number:", self.employee_number)
        print("Salary:", self.salary)
        
# Implementing the code from exam
new_student = Student("Anthony", "Smith", 35, "s346571")
new_student.get_stuinfo()

print("==========================")

new_employee = Employee("Sarah", "Taylor", 34, 2919736, 5000)
new_employee.get_empinfo()
