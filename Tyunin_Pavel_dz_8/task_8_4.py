from functools import wraps


def val_checker(some_check):
    def checker(func):
        @wraps(func)
        def check(x):
            if some_check(x):
                return func(x)
            else:
                raise ValueError('Wrong val', x)

        return check

    return checker


@val_checker(lambda x: x > 0)
def calc_cube(*args):
    return [arg ** 3 for arg in args]


a = calc_cube(-5)
print(a)
