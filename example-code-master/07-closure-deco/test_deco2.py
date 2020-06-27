from functools import wraps


def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)
    return wrapper


@my_decorator
def example(a, b, **kwds):
    """Docstring"""
    print("a = %d" % a)
    print("b = %d" % b)
    for i, j in kwds.items():
        print("%s = %d" % (i, j))
    print('Called example function')


example(10, 12, k=10, me=55)
print(example.__name__)
print(example.__doc__)
