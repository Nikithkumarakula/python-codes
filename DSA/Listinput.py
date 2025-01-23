# li=()
# num=int(input('Enter the count: '))

# for i in range(num):
#     ele=int(input(f'Enter element at index {i}  '))
#     li.append(ele)
# print(li)


li1 = input()
li1 = list(map(int,li1.split()))
print(li1)
print(list({i for i in li1 if i%2==0}))
