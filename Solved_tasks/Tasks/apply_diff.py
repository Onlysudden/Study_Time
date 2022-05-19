def apply_diff(a, dict):
	add_set = set(dict['add'])
	remove_set = set(dict['remove'])
	a.update(add_set)
	a.difference_update(remove_set)


target = {'a', 'b'}
diff = {'add': {'c'}, 'remove': {'a'}}
apply_diff(target, diff)
print(target)
