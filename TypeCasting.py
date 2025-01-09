
# if string 
a = "30"
print(a,type(a))
b=int(a)
print(b,type(b))


# str to integer conversion is not allowed.
x='kod'
print(x,type(x))
# y = int(x)
# print(y, type(y))

            #str to float convertion is not allowed
# p=float(input('enter float type data'))
# print(p,type(p))

#bool() 

'''1.While converting int to bool for non zero values we will get true
2.While converting int to bool for 0 we will get false
'''
q = 12
q=bool(q)
print(q,type(q))     #true

q = 'kod'
q=bool(q)
print(q,type(q))       #true


q = ''
q=bool(q)
print(q,type(q))         #false



print(bool(0))
print(bool(1))

print(int(12.56))   #12


