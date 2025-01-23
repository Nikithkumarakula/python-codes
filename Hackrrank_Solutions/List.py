li=[]
n=int(input())
for i in range(n):
    command,*values=input().split()  # insert 1 5
    values=list(map(int,values))
    # print(command)
    # print(values)
    if command=='insert':
        li.insert(values[0],values[1])
    elif command=='remove':
        li.remove(values[0])
    elif command=='append':
        li.append(values[0])
    elif command=='sort':
        li.sort()
    elif command=='print':
        print(li)
    elif command=='reverse':
        li.reverse()
    elif command=='pop':
        li.pop()
    else:
        print('Enter correct format')
        