from operator import index


def func_2(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

print(func_2(a=1, b=2, c=3))
