#Without input and without statement
def add():
    a=10
    b=20
    print('Addition is:',a+b)


#with input without return type
def sub(a,b):
    print('subtraction is: ',a-b)


# Without input and with return statement
def mul():
    return 10*20

def div(a,b):
    return a/b


add()
sub(10,5)
print(mul())
print(div(10,5))