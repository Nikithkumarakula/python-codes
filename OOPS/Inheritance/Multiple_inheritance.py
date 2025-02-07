'''class Demo1:
    def disp(self):
        print('inside disp1')
class Demo2:
    def disp(self):
        print('inside disp2')
class Demo3(Demo1,Demo2):
    pass

d3 = Demo3()
d3.disp3()                #Demo1.disp()
d3.disp()                  #MRO  Method Resolution Order

'''


'''class Demo1:
    def disp1(self):
        print('inside disp1')
class Demo2:
    def disp2(self):
        print('inside disp2')
class Demo3(Demo1,Demo2):
    pass

d3 = Demo3()
d3.disp1()           #disp1
d3.disp2()           #disp2
'''


#constructors are overidden methods
class Demo1:
    def __init__(self):
        self.x=100

class Demo2:
    # def __init__(self):
    #     self.x=200             #200
    pass
class Demo3(Demo2,Demo1):
    #def __init__(self):
        #self.x=300             #300
        pass

d3=Demo3()
print(d3.x)