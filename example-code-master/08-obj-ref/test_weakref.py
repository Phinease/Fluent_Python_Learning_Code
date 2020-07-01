import weakref

s1 = {1, 2, 5}
s2 = s1

if_end = weakref.finalize(s1, lambda: print("Dead"))

del s1
print(if_end.alive)
del s2
print('-' * 40)
print(if_end.alive)

a = {0, 1}
wref = weakref.ref(a)
print(wref)
print(wref())
_ = wref()
a = {1, 2}
print(wref())
print(wref() is None)
del _
print(wref())
print(wref() is None)

try:
    wref_list = weakref.ref([10, 20, 30])
except TypeError as err:
    print("Creat WeakRef of a list:", err)


class MyList(list):
    pass


my_l = MyList([10, 20, 30])
try:
    wref_list = weakref.ref(my_l)
    print("Creat WeakRef of MyList: Success")
except TypeError as err:
    print("Creat WeakRef of a list:", err)
