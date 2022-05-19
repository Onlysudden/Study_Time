def find_index(value, text):
	for index, elem in enumerate(text):
		if elem == value:
			return index


def find_second_index(value, text):
	cursor = iter(text)
	first_index = find_index(value, cursor)
	second_index = find_index(value, cursor)
	if second_index is not None:
		return first_index + second_index + 1


print(find_index('t', 'cat'))
print(find_index(5, [1, 2, 3, 4, 5, 6, 7]))
print(find_index(42, []))
print(find_index('!', 'abc'))

print(find_second_index(5, [1, 2, 3, 4, 5, 6, 7, 5]))
print(find_second_index(42, []))
print(find_second_index(3, (1, 2, 3, 4, 5, 6, 7, 5)))
