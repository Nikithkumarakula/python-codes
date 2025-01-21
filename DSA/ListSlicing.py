#list_name[start:end:steps]
li1=[10,20,30,40,50,60]
sub_li1 = li1[::]
print(sub_li1)    #[10, 20, 30, 40, 50, 60]

sub_li2 = li1[1:4:]
print(sub_li2)   #[20, 30, 40]

sub_li3 = li1[::2]
print(sub_li3)   #[10, 30, 50]

rev_li=li1[::-1]
print(rev_li)   #[60, 50, 40, 30, 20, 10]    reverse


print(li1[-1::]) #[60]    

'''
1.List Slicing can used to create sublist from main list.
Syntax: List_name[start:end-1:steps]

revese_list: [::-1]
last_ele: [-1::]
'''