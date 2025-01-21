
'''
1.In dict we cannot store duplicates keys
2.in dict we can store duplicate values
3.Dict are mutable
'''

d1 = {'name':'nikith',"age":27,'phone':25478}
print(d1,type(d1))  #{'name': 'nikith', 'age': 27, 'phone': 25478} <class 'dict'>

d1 = {'name':'nikith',"age":27,'phone':25478,'age':29}
print(d1,type(d1))  #{'name': 'nikith', 'age': 29, 'phone': 25478} <class 'dict'>


d1['age'] = 20
print(d1) #{'name': 'nikith', 'age': 20, 'phone': 25478}


marks={'sci':85,'mat':85}
print(marks)

marks={'mat':85,'mat':90}
print(marks)  #{'mat': 90}

marks={'mat':85,'mat':85}
print(marks)   #{'mat': 85}


for i in d1.keys():
    print(i)  #name  age phone

for i in d1.values():
    print(i)  #nikith  20  25478

for i in d1.items():
    print(i)    #('name', 'nikith')   ('age', 20) ('phone', 25478)



