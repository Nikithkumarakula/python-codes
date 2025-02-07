''' in python if we print reference variable then it will  display string representation of object
If the below example we have overriden __str__methods in their  respective classes

'''
class Demo1:
    def __str__(self):
        return 'Hello'
    def __sub__(self,other):
        self.a = 20
        other.b=10
        return self.a + other.b

class Demo2:
    def __str__(self):
        return 'Hii'
   


d1 = Demo1()
d2 = Demo2()
print(d1)
print(d2)


print(d1)  #  <__main__.Demo1 object at 0x00000186F3FA6A50>
print(d1 - d2)





