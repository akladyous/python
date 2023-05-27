from person import PersonalInfo

class Student(PersonalInfo):
    def __init__(self, first_name, last_name, age, residence, grade, courses):
        super().__init__(first_name, last_name, age, residence)
        self.grade = grade
        self.courses = courses

    def getInfo(self):
        super(Student, self).getInfo()
        print(f"dati STUDENT :\nGrade:\t\t{self.grade}\nCourses\t\t{self.courses}\n")
        


s1=Student('david', 'akladyous', 15, 'florida', 10, 'english')


s1.getInfo()