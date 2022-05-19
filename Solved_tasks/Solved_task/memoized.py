def memoized(function):
    memory = {}

    def inner(num):
        if num not in memory:
            memory[num] = function(num)
        return memory[num]
    return inner


@memoized
def f(x):
    print('Calculating...')
    return x * 10


print(f(1))
print(f(1))
print(f(42))
print(f(42))
print(f(1))
