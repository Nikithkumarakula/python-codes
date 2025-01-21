'''
1.In tuples we can store homogenious and hetrogenious data
2.tuples can store duplicates also
3.tuples are ordered collection of data
4.Tuples are immutable: Once delared the tuple we cannot change(modify) it.

'''


tup = (10,20,30,'kodnest', True , 20,30,50,65)
print(tup)#(10, 20, 30, 'kodnest', True, 20, 30)


#tup.remove(65)
#tup.pop()
# del tup[2]

print(tup[2])#30


#del tup


t1 = (1,2,3)
t2 = (4,5,6)
tup = t1+t2
print(tup)  #(1, 2, 3, 4, 5, 6)



#create a singleton tuples
tup=(10)   #10 <class 'int'>
tup = (10,)
print(tup,type(tup)) #(10,) <class 'tuple'>


#packing and unpacking

tup1 = (10,20,30,40)
#unpacking
ele1,el2,ele3,ele4 = tup1
print('Value of ele',ele1)