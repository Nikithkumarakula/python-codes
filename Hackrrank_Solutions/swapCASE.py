'''

s=input().split()
for i in s:
    if i.lower():
        i.upper()
    if i.upper():
        i.lower()
'''

def swapcase(s):
    sample=''
    for i in s:
        if i.islower():
            sample = sample + i.upper()
        else:
            sample = sample + i.lower()
    return sample

print(swapcase(input()))

