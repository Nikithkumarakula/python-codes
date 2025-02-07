'''
To determine the accessbility of data members,member functions
public   a
protected    _a
private   __a
'''


class Demo1:
    def __init__(self,name):
        self.name = name
    def disp1(self):
        print(self.name)
d1 = Demo1('Akash')

class Demo2(Demo1):
    def disp2(self):
        print(d1.name)
d2 = Demo2('Pooja')

print(d1.name)
print(d2.name)
d1.disp1()
d2.disp2()



# The variable which are public can be access insid the same class,outside the class , inside the child class,  inside the non-child class
# outside anywhere inside,outside,child class
