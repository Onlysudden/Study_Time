def greet(name, surname):
    return 'Hello, {name} {surname}!'.format(name=name, surname=surname)


def partial_apply(function, arg1):
    def inner(arg2):
        return function(arg1, arg2)
    return inner


f = partial_apply(greet, 'Dorian')
print(f('Grey'))


def flip(function):
    def inner(arg1, arg2):
        arg1, arg2 = arg2, arg1
        return function(arg1, arg2)
    return inner


f = flip(greet)
print(f('Christian', 'Teodor'))
