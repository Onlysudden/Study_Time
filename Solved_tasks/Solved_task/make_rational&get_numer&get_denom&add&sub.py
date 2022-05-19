from math import gcd


def make_rational(numer, denom):
    divider = gcd(numer, denom)
    return "{}/{}".format(numer // divider, denom // divider)


def get_numer(rat):
    numer, _ = rat.split('/')
    return numer


def get_denom(rat):
    _, denom = rat.split('/')
    return denom


def add(x1, x2):
    denom = int(get_denom(x1)) * int(get_denom(x2))
    numer = (
        int(get_numer(x1)) * int(get_denom(x2))
        + int(get_numer(x2)) * int(get_denom(x1)))
    divider = gcd(numer, denom)
    return "{}/{}".format(numer // divider, denom // divider)


def sub(x1, x2):
    denom = int(get_denom(x1)) * int(get_denom(x2))
    numer = (
        int(get_numer(x1)) * int(get_denom(x2))
        - int(get_numer(x2)) * int(get_denom(x1)))
    divider = gcd(numer, denom)
    return "{}/{}".format(numer // divider, denom // divider)


def rat_to_string(rat):
    return str(rat)


rat1 = make_rational(3, 9)
print(get_numer(rat1))
print(get_denom(rat1))

rat2 = make_rational(10, 3)

rat3 = add(rat1, rat2)
print(rat_to_string(rat3))

rat4 = sub(rat1, rat2)
print(rat_to_string(rat4))
