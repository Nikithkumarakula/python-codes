class Demo1:
    def disp1(self):
        print('Inside the disp1')
class demo2(Demo1):
    def disp2(self):
        print('inside disp2')

class Demo3(Demo1):
    def disp3(self):
        pass

d1 = Demo3()
d1.disp1()
