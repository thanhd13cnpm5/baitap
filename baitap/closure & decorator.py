#closure

def funcA(val1):
    def funcB(val2):
        return val1*val2

    return funcB

f1 = funcA(5)
f2 = funcA(4)
print(f1(f2(3)))


#decorator
def decor2(func):
    def inner():
        x = func()
        return x ** 2
    return inner

def decor1(func):
    def inner():
        x = func()
        return x * x

    return inner

def decor(func):
    def inner():
        x = func()
        return 2 * x

    return inner


@decor1# result 160000
@decor2# result 400
@decor# result 20
def num():
    return 10

print(num())

@decor1 # result 400
@decor# result 20
def num():
    return 10

print(num())

#lambda

x = lambda x, y: x**y
print(x(4, 4))