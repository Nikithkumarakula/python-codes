class Demo1:
    def __init__(self,name):
        self.__name = name
    
d1 = Demo1('Akash')
print(d1._Demo1__name)     #Pyhon does not allow the encapsulation

# private variable 




'''
Name mangling is the process of providing new name to the private variables
these new names will be automatically by python for all private members 
New Name will be provided in the format:ObjectName._className__variableName

'''