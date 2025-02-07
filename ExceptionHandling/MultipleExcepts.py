def disp(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print('Zero divisionError occured')              # without sudden terminations
    except NameError:
        print('Name error occured')
    except TypeError:
        print('Type error occured')
    except:
        print('some error occure')

disp(10,20)
disp(10,'kodnest')