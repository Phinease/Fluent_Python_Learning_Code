import numbers
import collections
import abc


x = 30
y = [20, 30]
print(type(x))


def f(x):
    if isinstance(x, int):
        x += 20
    if isinstance(x, list):
        x += [20]
    return x


print(f(x))
print(x)
print(f(y))
print(y)