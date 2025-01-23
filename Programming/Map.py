# map(function, iterable_object)

def double(x):
    return x*2
li=[1,5,3,4]
double_li = list(map(double,li))
print(double_li)   #  [2, 10, 6, 8]

tup = ('10','20','50','25')
new_tuple=tuple(map(int,tup))
print(new_tuple)   # (10, 20, 50, 25)

li2 = [1,5,66]
ne_li2 = list(map(float,li2))
print(ne_li2)  # [1.0, 5.0, 66.0]