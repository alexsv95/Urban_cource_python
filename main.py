# import math
#
# def square(x):
#     a = x ** 2
#     print(globals())
#     return a
#
# a = 5
# b = square(2)
# print(b)
# print(globals())
#
d = 10

print(d)

def square(x):
    d = x + 2
    def even(x):
        nonlocal d
        d = x / 2
        if d % 2 == 0:
            print('Четное')
        else:
            print('Нечетное')
    even(x)
    return d


print(square(4))