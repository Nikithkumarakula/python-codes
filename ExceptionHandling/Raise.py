# def disp(a,b):
#     print(a/b)
# disp(10/'kodnest')


def checkAge(age):
    if(age<18):
        raise ValueError("Age must be greater than 18")
try:
    checkAge(20)
except ValueError as e:
    print('error:',e)
