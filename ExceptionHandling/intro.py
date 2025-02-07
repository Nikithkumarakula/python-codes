def disp(a,b):
    try:
        print('Task started')
        print(a/b)
    except:
        print('some error handled')
    else:
        print('Task execution without exception')
    finally:
        print('Task ended')
disp(10,0)
disp(10,5)
disp(20,2)



'''
Try: used to keep the logic in which get some error
except: will be executed when exception occure in try block logic
else: will be executed thre is try logic will be executed without any error
finally:  will always executed, it=rrespective of exception occure or not.
'''