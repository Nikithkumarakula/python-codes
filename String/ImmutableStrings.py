
# s1 = 'kodnest'
# s1.upper()
# print(s1)

'''1.Strings are immutable : Once we can declare a string does not modify it,if we try to modify the strings it will create new string.
2.If new string does not have any reference variable then it will be removed
3.python internally uses String interning
4.The process is checking strig intern pool before creating any new object
5.whenever to create new object python first to check intern to weather that object already exist or not
6.when the object already present string intern records then address of existing object will be refused'''


# s1='K'
# print(s1, id(s1))

#actual address of the objects

s1='Hello'
s2='World'
print(s1, id(s1))
print(s2, id(s2))

print('s1',s1[0],id(s1[0])) #H
print('s2',s2[0],id(s2[0]))


print('s1',s1[-1],id(s1[-1])) #o
print('s2',s2[1],id(s2[1]))


print('s1',s1[2],id(s1[2]))
print('s1',s1[3],id(s1[3]))