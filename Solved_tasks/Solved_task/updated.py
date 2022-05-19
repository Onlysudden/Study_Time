def updated(book, **kwargs):
	b = {}
	b.update(book)
	b.update(kwargs)
	return b


d = {'a': 1, 'b': False}
print(updated(d, a=2, b=True, c=None))
print(d)
print(updated(d) == d)
print(updated(d) is d)
