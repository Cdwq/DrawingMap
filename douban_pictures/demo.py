def decorator_a(func):
    print('Get in decorator_a')

    def inner_a(*args, **kwargs):
        print('Get in inner_a')
        return func(*args, **kwargs)

    return inner_a


def decorator_b(func):
    print('Get in decorator_b')

    def inner_b(*args, **kwargs):
        print('Get in inner_b')
        return func(*args, **kwargs)

    return inner_b


@decorator_b
@decorator_a
def f(x):
    print('Get in f')

    return x * 2


# f(1)

import numpy as np
a = np.array([[2, 4, 6], [4, 8, 12]])
print(np.var(a,axis=1))