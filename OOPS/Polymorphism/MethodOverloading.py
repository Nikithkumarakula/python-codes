class Calculator:
    def add(self,a,b,c=0):
        return a+b+c

cal=Calculator()
print(cal.add(10,20))
print(cal.add(10,20,30))
#cal.add(10,20,30,40)
