import threading
import time
li1 = [1,2,3,4,5]
li2 = ['a','b','c','d','e']

def disp1(li1):
    print(threading.current_thread())
    for i in li1:
        print(i)
        time.sleep(1)
def disp2(li2):
    print(threading.current_thread())
    for i in li2:
        print(i)
        time.sleep(1)

t1 = threading.Thread(target=disp1,args=(li1,), name='Tester')    
t2 = threading.Thread(target=disp2,args=(li2,), name='Developer')
#(li1,)  tuple arguments
t1.start()
print(t1.is_alive())
t1.join()
print(t1.is_alive())

t2.start()
