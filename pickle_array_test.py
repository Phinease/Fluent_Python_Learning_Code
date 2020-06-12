import timeit

SETUP = """
from array import array
from random import random

f = array('d', (random() for i in range(10 ** 7)))
file = open('test.bin', 'wb')
f.tofile(file)
file.close()
"""

test = """
ff = array('d')
file = open('test.bin', 'rb')
ff.fromfile(file, 10 ** 7)
file.close()
print(ff == f)
"""

res = timeit.timeit(test, setup=SETUP, number=5)
print("Time:", res/5, "s")


SETUP = """
from array import array
from random import random
import pickle

f = array('d', (random() for i in range(10 ** 7)))
file = open('test.bin', 'wb')
pickle.dump(f, file)
file.close()
"""
test = """
file = open('test.bin', 'rb')
ff = pickle.load(file)
file.close()
print(ff == f)
"""

res = timeit.timeit(test, setup=SETUP, number=5)
print("Time:", res/5, "s")
