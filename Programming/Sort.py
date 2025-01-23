# sort In original list will modified

li = [10,80,65,1,28,35]
li.sort()
print(li)  #[1, 10, 28, 35, 65, 80]

li.sort(reverse=True)
print(li)    #  [80, 65, 35, 28, 10, 1]


#sorted(li) in another list
li2=[1,85,24,65,12,48,35]
sorted(li2)
print(li2)   # [1, 85, 24, 65, 12, 48, 35]


sorted_li=sorted(li2)
print(sorted_li)    #  [1, 12, 24, 35, 48, 65, 85]