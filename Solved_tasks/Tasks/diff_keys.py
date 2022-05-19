def diff_keys(book1, book2):
	result = {}
	set1 = set(book1.keys())
	set2 = set(book2.keys())
	result['kept'] = set1 & set2
	result['added'] = set2 - set1
	result['removed'] = set1 - set2
	return result


book1 = {'name': 'Bob', 'age': 42}
book2 = {}

print(diff_keys(book1, book2))

book1 = {}
book2 = {'name': 'Bob', 'age': 42}

print(diff_keys(book1, book2))

book1 = {'a': '2'}
book2 = {'a': '1'}

print(diff_keys(book1, book2))
