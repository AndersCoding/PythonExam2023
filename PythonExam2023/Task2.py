# Task 2

class Student:
    passingMark = 50  # Class variable, 50 being the score needed to pass

    def __init__(self, name, mark):  # Constructor with instance variables
        self.name = name
        self.mark = mark

    def __str__(self):  # Formatted string returning name and mark of student
        return f"Name: {self.name}, mark: {self.mark}"

    def passOrFail(self):  # Method for verifying if the student has passed, or not
        if self.mark >= Student.passingMark:
            return "Pass"
        elif self.mark < Student.passingMark:
            return "Fail"

# The students with their marks
student1 = Student("John", 52)
status1 = student1.passOrFail()
student2 = Student("Jenny", 69)
status2 = student2.passOrFail()

# Printing the result for the students
print("Marks needed to pass = 50")
print(f"{student1} -> " + status1)
print(f"{student2} -> " + status2)

# Updating the passingMark
Student.passingMark = 60

# The students with their first marks
status1 = student1.passOrFail()
status2 = student2.passOrFail()

# Printing the result for the students
print("\nMarks needed to pass = 60")
print(f"{student1} -> " + status1)
print(f"{student2} -> " + status2)