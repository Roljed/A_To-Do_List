class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.student_id = self.calculate_id()

    def calculate_id(self):
        return self.name[0] + self.last_name + str(self.birth_year)


i_name = input()
i_last_name = input()
i_birth_year = input()

student = Student(i_name, i_last_name, i_birth_year)
print(student.student_id)
