li1=[1,2,3,4,5]
print(li1)

#  Syntax:[Expression for i in iterable_object condition]
sq_li=[]
for i in li1:
    sq_li.append(i**2)
print(sq_li)

sq_li=[i**2 for i in li1]
print(sq_li)

new_li = [i+1 for i in li1]
print(new_li)


#when we have only if part then write it after for loop
even=[i for i in li1 if i%2==0]
print(even)


#when we hava if-else both write it before for loop
even_odd=['even' if i%2==0 else 'odd' for i in li1]
print(even_odd)


li2=[-5,-7,0,5,9,-6]
#positive_negative = ['positive' if i>0 elif i<0 'Negative' else 'zero' for i in li2]
positive_negative = ['positive' if i > 0 else 'negative' if i < 0 else 'zero' for i in li2]
print(positive_negative)


li = [[10,20],[30,40],[50,60]]
new_li = [ele for sublist in li for ele in sublist]
print(new_li)     #   [10, 20, 30, 40, 50, 60]