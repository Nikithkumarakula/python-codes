'''
1.reverse()  reverse origial object
2.reversed()  method reversed with the help of another new object
'''


li = [10,50,90,40,60]
print("Before reverse",li)  #[60, 40, 90, 50, 10]
li.reverse()
print("After reverse",li)  #[60, 40, 90, 50, 10]


li2 = [11,5,8,44,66]
reverse_li2=reversed(li2)
print(reverse_li2) # list_reverseiterator object
reverse_li2=list(reversed(li2))
print("After reverse",reverse_li2) #After reverse [66, 44, 8, 5, 11]