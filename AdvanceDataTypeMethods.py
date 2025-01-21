li = list('Kodnest')
print(li)    #  ['K', 'o', 'd', 'n', 'e', 's', 't']

li2 = list((10,20))
print(li2)     #   [10, 20]

li3 = list({100,200})
print(li3)    #   [200, 100]


li4 = list({'name':'ak','age':22})
print(li4)   #  ['name', 'age']


li5 = list(range(1,10))
print(li5)   #  [1, 2, 3, 4, 5, 6, 7, 8, 9]


tup1 = tuple([10,20,30])
print(tup1)   #(10, 20, 30)
tup1 = tuple({10,20})
print(tup1)   #(10, 20)

tup1 = tuple({'name':'ak','age':22})
print(tup1) #('name', 'age') 

tup1 = tuple('kodnest')
print(tup1)   #('k', 'o', 'd', 'n', 'e', 's', 't')

tup1 = tuple(range(5,10))
print(tup1)  #(5, 6, 7, 8, 9)

s1 = set([10,20,30,50])
print(s1)   # {10, 20, 50, 30}


d1 = dict([['name','ak'],['age',50]])
print(d1)   #  {'name': 'ak', 'age': 50}
