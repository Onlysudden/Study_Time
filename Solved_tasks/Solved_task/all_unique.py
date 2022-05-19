def all_unique(book):
	set_book = set(book)
	if len(set_book) != len(book):
		return False
	return True


print(all_unique('cat'))
print(all_unique([1, 2, 3]))
print(all_unique([1, 2, 1]))