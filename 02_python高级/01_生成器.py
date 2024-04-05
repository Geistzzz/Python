# iterable object
def hello_world():
    print("hello world1")
    yield 1
    print("hello world2")
    yield 2
    print("hello world3")
    yield 3


g = hello_world()
res = next(g)
print(res)
res = next(g)
print(res)
res = next(g)
print(res)


def squares(counts):
    for num in range(1, counts + 1):
        yield num ** 2


for i in squares(10):
    print(i)
