
'''
1.Set can store hemogneous and hetrogenious data
2.set is unordered collection of data
3.set does not support indexing of data
4.Set does not allowes the duplicates
'''

s1={10,20,'kodnest',True,10,20,90,64}
print(s1,type(s1))#{64, True, 'kodnest', 20, 90, 10} <class 'set'>

#print(s1[0])   #error:'set' object is not subscriptable

s1.add(500)
print(s1)#{64, True, 20, 90, 500, 10, 'kodnest'}

s1.remove(500)
print(s1)#{64, True, 20, 90, 'kodnest', 10}


'''With index have methods not accepted in set'''
#pop() without index delete one elment and give the deleted element
poped_ele=s1.pop()
print(poped_ele)
print(s1)