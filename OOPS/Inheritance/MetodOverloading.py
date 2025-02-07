class Demo:
    def disp(self):
        print('Inside disp')
    def disp(self,a):
        print('inside disp with 1 para')
    def disp(self,a,b,):
        print('inside disp with 2 para')

d = Demo()
#d.disp()
#d.disp(10)
d.disp(10,20)


'''Only last one , python does not support the method overloading'''
    