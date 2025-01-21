# Enumarate values


'''li = [10,20,30]    --> without enumarate it give erroor unpacking 
for ind,ele in li:
    print(ind,ele)'''

li = [10,20,30]
for ind,ele in enumerate(li):
    print(ind,ele)

#write python program to print all even index elements

for ind,ele in enumerate(li,start=1):
    if ind%2==0:
        print(ind,ele)
        