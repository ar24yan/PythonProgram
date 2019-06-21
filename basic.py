class Student:
    def __init__(self, name, rollNo):
        self.name = name
        self.rollNo = rollNo
    def get(self):
        print("Name of the student is",self.name)
        print("Roll number of the student is",self.rollNo)

s = Student("Aryan", 110)
s.get()
