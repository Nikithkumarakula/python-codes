"""li = list(map(int,input().split(",")))
li = list(set(li))
# li = list(li)  --> sort wont return anything
li.sort()
print("Largest element:",li[-1])
print("Second Largest element:",li[-2])
print("Smallest element:",li[0])"""

'''Packing and Unpacking'''
#name,marks = ['pooja',15,40,35]
name,*marks = ['pooja',15,40,35]
name,*marks,age = ['rahul',75,100,85,24]
print(name,marks)



