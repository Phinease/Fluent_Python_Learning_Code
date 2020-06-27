b = 6


def f(x):
    global b
    print(x)
    print(b)
    b = 10


f(5)
print(b)