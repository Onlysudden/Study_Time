def count_all(coub):
	diction = {}
	for elem in coub:
		if elem not in diction:
			diction[elem] = 1
		else:
			diction[elem] += 1
	print(diction)


count_all(['cat', 'dog', 'cat'])
count_all('hello')
count_all('*' * 20)
