from functools import wraps


def memoizing(length):
    memory = {}
    keys = []

    def wrapper(function):
        @wraps(function)
        def inner(num):
            if num not in memory:
                if len(keys) == length:
                    memory.pop(keys.pop(0))
                    memory[num] = function(num)
                    keys.append(num)
                else:
                    memory[num] = function(num)
                    keys.append(num)
            return memory[num]
        return inner
    return wrapper


@memoizing(3)
def f(x):
    """
    Наша функция!
    """
    print('Calculating...')
    return x * 10


print(f(1))
print(f(1))
print(f(2))
print(f(3))
print(f(4))
print(f(1))
print(f(4))
help(f)
