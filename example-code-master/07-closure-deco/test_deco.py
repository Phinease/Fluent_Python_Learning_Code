def deco(func):
    print("Running Deco")
    return func


@deco
def target():
    print("Running Target")


target()
print('-'*30)
print(target)
