def make_user(name, age):
	dictionary = {
		name: age
	}
	return dictionary


def format_user(diction):
	for k, v in diction.items():
		print(k, v)


phil = make_user('Phil', 25)
print(type(phil))
format_user(phil)
