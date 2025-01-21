'''
1.Conditional: if-else, if-elif
2.looping: for, while
3. Jumping: break, continue, pass
'''

'''def checkAge(age):
    if(age>18):
        print('Age is greater than 18')
    else:
        print('Age is not greater than 18')
checkAge(19)'''

def ageCata(age):
    if(age<18):
        print('child')
    elif(age>18 and age<65):
        print('Adult')
    elif(age>65):
        print('senior cetigen')
ageCata(int(input('Enter the age')))