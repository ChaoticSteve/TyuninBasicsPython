from functools import wraps


def type_logger(func):
    @wraps(func)
    def tag_logger(*args):
        message = ''
        for arg in args:
            message += f'{func.__name__} ({arg}: {type(arg)})\n'
        return message

    return tag_logger


@type_logger
def calc_cube(*args):
    return [arg ** 3 for arg in args]

if __name__ == '__main__':
    a = calc_cube(5, 3, 6)
    print(a)

