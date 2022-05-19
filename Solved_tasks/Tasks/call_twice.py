def call_twice(f, *args, **kwargs):
    first_f = f(*args, **kwargs)
    second_f = f(*args, **kwargs)
    return first_f, second_f


print(call_twice(input, 'Enter value: '))
