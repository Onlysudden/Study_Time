def is_even(x):
    if x == 0:
        return True

    else:
        return is_odd(x - 1)


def is_odd(x):
    return not is_even(x)


print(is_odd(3))
print(is_odd(42))
print(is_odd(99))
print(is_even(42))
print(is_even(99))
print(is_even(3))
