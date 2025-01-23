# s = 'kodnest'
# s=s.replace(int('5'),'A')
# print(s)

def mutations(s,posi,ch):
    li=list(s)
    li[posi] = ch
    res=''.join(li)
    return res
    

s = input()
p,c = input().split()
print(mutations(s,int(p),c))



