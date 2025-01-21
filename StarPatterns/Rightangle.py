#right angle    increaseing pattern (i+1)

row=4
col=5
for i in range(row):
    for j in range(i+1):
        print('*',end='')
    print()


#reverse right angle   decreasing pattern (i,row)
for i in range(row):
    for j in range(i,row):
        print('*',end='')
    print()


# right pascle triangle

print('right angle pascle')

for i in range(row):
    for j in range(i+1):
        print('*',end='')
    print()

for i in range(row):
    for j in range(i,row-1):
        print('*',end='')
    print()
