from operator import *


def keep_truthful(iterator):
    result = []
    for elem in iterator:
        if truth(elem):
            result.append(elem)
    return result


print(list(keep_truthful([True, False, '', 'foo'])))


def abs_sum(iterator):
    sum = 0
    for elem in iterator:
        sum += abs(elem)
    return sum


print(abs_sum([-3, 7]))
print(abs_sum([]))
print(abs_sum([42]))


def walk(book, path):
    result = book.copy()
    for elem in path:
        result = result.get(elem)
    return result


print(walk({'a': {7: {'b': 42}}}, ['a', 7, 'b']))
print(walk({'a': {7: {'b': 42}}}, ['a', 7]))
