'''
Contructor chaining is the process of one constructor from another constructor
'''

class grandParent:
    def __init__(self):
        self.x=100

class Parent(grandParent):
    def __init__(self):
        self.y=200
        super().__init__()

class child(Parent):
    def __init__(self):
        self.z=300
        super().__init__()

c=child()
print(c.z)
print(c.y)
print(c.x)
p=Parent()
print(p.x)
