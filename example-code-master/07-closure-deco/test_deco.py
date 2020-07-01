def deco(func):
    print("Running Deco")
    return func


@deco
def target():
    print("Running Target")


target()
print('-'*30)
print(target)


def deco2(a=2):
    def decorate(func):
        return func()
    print(a)
    return decorate


print('-'*30)
deco2(a=10)(target)
