from copy import deepcopy
import inspect

x = {'name': 'CHEN Shuangrui', 'age': 999, 'list': [10, 20]}

print(dir(x))
print(id(x))
print(x.__hash__)

print('-' * 40)
y = x.copy()
x['name'] = "Me"
x['list'] += [10, 20]
print(y)
print(x)

z = dict(x)
x['age'] = 10
x['list'] += [90.20]
print(x)
print(z)

k = deepcopy(x)
x['list'] += [52.23]
print(x)
print(k)

print('-' * 40)

a = [20, 50, 30]
b = list(a)
a += [999, 888]
print("a:", a, "id:", id(a))
print("b:", b)
c = a
print("c:", c, "id:", id(c))
del a
print("b:", b)
print("c:", c, "id:", id(b))
try:
    print("a:", a)
except NameError:
    print("a: Name Error")

'''
How to inspect source code
'''
for i in inspect.getsourcelines(deepcopy)[0]:
    print(i, end='')
print('-'*40)

