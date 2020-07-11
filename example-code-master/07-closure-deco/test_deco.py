def deco(func):
    count = 0
    print("This is a decorator. No.%d" % count)
    func()
    count += 1
    print("After deco. No.%d" % count)


@deco
def hello():
    print("Hello")
