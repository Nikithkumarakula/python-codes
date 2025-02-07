import threading
import time

def back_task():
    while True:
        print('Background task running...')
        time.sleep(1)

t1 = threading.Thread(target=back_task)
t1.daemon = True
t1.start()

time.sleep(3)
print('main program ends.')
