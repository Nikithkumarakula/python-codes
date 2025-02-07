class Demo1:
    def disp1(self):
        print('inside disp1')

class Demo2(Demo1):
    pass

d2 = Demo2()
d2.disp1()