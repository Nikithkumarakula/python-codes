'''
if abstract class does not have any method then object for the abstract class can be created

if abstarct class can be created and concreate methods can be invoked
'''


from abc import ABC, abstractmethod
class Demo1(ABC):
    pass
    # @abstractmethod
    # def disp1(self):
    #     print('Inside disp1')


d1 = Demo1()

class Demo2(ABC):
    def disp(self):
        print('Inside disp2')

d2 = Demo2()
d2.disp()



class Demo3(ABC):
    def info(self):
        print('Inside info')
    @abstractmethod
    def disp3(self):
        print('inside disp3')
class Demo4(Demo3):
    pass
d4 = Demo4()
d4.info()


