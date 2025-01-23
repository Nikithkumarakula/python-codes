# s=input('ABCDCDC')
# sub_str=input('CDC')

# count=0
# n=len(s)-len(sub_str)+1

# for i in range(n):
#     if s[i:len(sub_str)+i] == sub_str:
#         count = count+1
# print(count)


def count_substring(string, sub_string):   
    n=len(string)-len(sub_string)+1
    count=0
    for i in range(n):
        if string[i:len(sub_string)+i]==sub_string:
            count=count+1 
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)