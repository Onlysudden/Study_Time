def greet(name, *args):
	list = []
	for elem in (name,) + args:
		list.append(elem)
	result = f"Hello, {' and '.join(list)}!"
	print(result)


greet('Bob', 'Mary')
greet('Bob')
greet(*'ABC')
