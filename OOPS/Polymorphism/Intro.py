
#Polymorphism
#method overriding

class Calculator:
    def calculate(self,a,b):
        print('Calculate result of a and b')

class Add(Calculator):
    def calculate(self, a, b):
        print('Addition: ', a+b)
        #return super().calculator(a, b)

class Sub(Calculator):
    def calculate(self, a, b):
        print('Subtraction: ', a-b)
class Mul(Calculator):
    pass

ref=Add()
ref.calculate(10,20)

ref=Sub()
ref.calculate(10,20)

ref=Mul()
ref.calculate(10,20)  # Calculate result of a and b


'''
def permit(ref,a,b):
    ref.calculate(a,b)

permit(Add(),10,20)
permit(Sub(),10,20)
Add().calculate(10,50)




# DUCk TYPING
class Add():
    def calculate(self, a, b):
        print('Addition: ', a+b)

class Sub():
    def calculate(self, a, b):
        print('Subtraction: ', a-b)

class Mul():
    pass


def permit(ref,a,b):
    if type(ref).__name__ == 'Mul':
        print(type(ref))
        print('Mul class does not have calculate method')
    else:
        ref.calculate(a,b)

permit(Add(),10,20)
permit(Sub(),10,20)

permit(Mul(),10,20)

'''