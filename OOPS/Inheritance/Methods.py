class Student:
    def cook(self):
        print("Student is cooking")
    def play(self):
        print("playing cricket")

class Employee(Student):
    def Work(self):
        print("Employee Working")
    def cook(self):
        print("Employee is cooking")


e=Employee()
e.play()


'''
work():Specilized method  -->Only in child class
cook():overriden method   -->we will impliment the parent to child class
play():inherited Metod     -->call the same in the parent method
'''