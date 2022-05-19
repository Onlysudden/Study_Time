from math import sqrt


def get_square_roots(number):
	result = []
	sqrt_number = sqrt(number)
	result.extend([-sqrt_number, sqrt_number])

	return result


def get_range(n):
	result = []
	i = 0
	if n > 0:
		for i in range(n):
			result.append(i)
	return result


print(get_square_roots(9))
print(get_square_roots(25))
print(get_square_roots(10001))

print(get_range(5))
print(get_range(10))
print(get_range(0))
