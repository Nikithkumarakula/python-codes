
'''
1.In list we can store Homogenious as well as hetrogenious data.
2.In list we can have duplicate values
3.List is an Ordered Collection of data:Order of insertion will remain as it is in the output
4.List is Mutable: once we declare the list we can modify it.

'''

li = [1,2,4,"kodnest",True,20]
print(li)


#append(): will add element at the end of the list -->(Mutable)
li.append(300)
print(li)  #[1, 2, 4, 'kodnest', True, 20, 300]

print(li[0])  #1

li.insert(1,"Ramu")
print(li)  #[1, 'Ramu', 2, 4, 'kodnest', True, 20, 300]

li.remove(4)
print(li)  #[1, 'Ramu', 2, 'kodnest', True, 20, 300]

# remove (ele): remove the first occurance of the specific element
# li.remove(input())
# print(li)   # 800 x not in list

# in or not in
print(300 in li)
print(200 not in li)


# without argument will delete and return last ele. from list
remove_ele = li.pop()
print(remove_ele)
print(li)


#pop(index) with argument will delete and return specified index
remove_ele = li.pop(3)
print(remove_ele)
print(li)


li.insert(3,"kodnest")
print(li)


#del keyword : without store the delete elements

del li[2]
print(li)

#del li
print(li)  #'li' is not defined


l1=[1,2,3]
l2=[4,5,6]
li=l1+l2

print(li)
