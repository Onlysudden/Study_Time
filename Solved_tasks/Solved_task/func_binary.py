def binary(number):
	result = ''
	while number >= 0:
		if number == 0:
			result += '0'
			return result[::-1]

		elif number == 1:
			result += '1'
			return result[::-1]

		modulo = number % 2
		number //= 2
		result += str(modulo)


print(binary(8))
