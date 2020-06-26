import timeit
from dis import dis

it1 = timeit.timeit("x = set([1, 2, 3])", number=100000)
it2 = timeit.timeit("x = {1, 2, 3}", number=100000)

print(it1)
print(it2)
print(dis('import matplotlib.pyplot as plt'))
