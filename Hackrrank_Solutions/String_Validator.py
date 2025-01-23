'''
s='kodnest'
print(s.isalnum())   #True

s='kodnest#'
print(s.isalnum())     #false

s='kodnest'
s1='kodnest23'
print(s.isalpha())   #True
print(s1.isalpha())   #False


s='123'
print(s.isdigit())   #true
print('12ad'.isdigit())   #false
print(s.islower())

print(any([(True,False,False,True)]))   #true
'''


s = input() 
print(any([i.isalnum() for i in s]))
print(any([i.isalpha() for i in s]))
print(any([i.isdigit() for i in s]))
print(any([i.islower() for i in s]))
print(any([i.isupper() for i in s]))

