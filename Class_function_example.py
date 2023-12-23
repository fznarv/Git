class Student:
    def __init__(self, name, mathG, scieG, englG):
        self.name = name
        self.mathG = mathG
        self.scieG = scieG
        self.englG = englG

    def average(self):
        return (self.mathG + self.scieG + self.englG) / 3

# Example of creating a Student instance
name_input = input("Enter student's name: ")
math_grade = float(input("Enter math grade: "))
science_grade = float(input("Enter science grade: "))
english_grade = float(input("Enter English grade: "))

student = Student(name_input, math_grade, science_grade, english_grade)
average_grade = student.average()

print(f"Student Name: {student.name}")
print(f"Average Grade: {average_grade:.2f}")


