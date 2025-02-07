class Employee:
    company_name='code'
    def __init__(self,name,age,desi):
        self.name=name
        self.age=age
        self.desi=desi

    def login(self,time):
        print(f'{self.name} logged in at {time}')


    def logout(self,time):
        print(f'{self.name} loggedout in at {time}')

    def work(self,hours):
        print(f'{self.name} worked for {hours}')

    def getDetails(self):
        print('Employee Nmae: ', self.name)
        print('Employee Age: ',self.age)
        print('Employee Designation: ',self.desi)

e1=Employee('ramu',20,'Soft Eng')
e2 = Employee('pk',25,'Developer')

# Employee.login(e1,'10:30')
# Employee.work(e1,"10 hours")
# Employee.logout(e1,'05:00')


# Employee.login(e2,'10:30')
# Employee.work(e2,"10 hours")
# Employee.logout(e2,'05:00')

e1.getDetails()
e2.getDetails()

e1.login("10:30")
e1.work("10 hours")
e1.logout("05:00")
