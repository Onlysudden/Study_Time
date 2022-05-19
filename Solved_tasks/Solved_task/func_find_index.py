def find_index(str, list):
	for (index, elem) in enumerate(list):
		if elem == str:
			return index
			break
	else:
		return None


print(find_index('t', 'cat'))
print(find_index(5, [1, 2, 3, 4, 5, 6, 7]))
print(find_index(42, []))
print(find_index('!', 'abc'))
