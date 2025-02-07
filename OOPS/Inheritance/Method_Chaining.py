'''
Contructor chaining is the process of one constructor from another constructor
'''

'''class grandParent:
    def grand(self):
        self.x=100

class Parent(grandParent):
    def parent(self):
        self.y=200
        super().grand()

class child(Parent):
    def child(self):
        self.z=300
        super().parent()

c=child()
print(c.z)
print(c.y)
print(c.x)
'''
class GrandParent:
    def cook(self):
        print("GrandParent cook biriyani")

class Parent(GrandParent):
    def cook(self):
        print("Parent cook Maggi")
       # super().cook()
class Child(Parent):
    def cook(self):
        print("child not cook ")
        super().cook()

        super(Parent,self).cook()

c=Child()
c.cook()
#
# print(c.cook())
