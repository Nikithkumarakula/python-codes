import time
li1 = [1,2,3,4,5]
li2 = ['a','b','c','d','e']

def disp1(li1):
    for i in li1:
        print(i)
        time.sleep(1)
def disp2(li2):
    for i in li2:
        print(i)
        time.sleep(1)

disp1(li1)
disp2(li2)