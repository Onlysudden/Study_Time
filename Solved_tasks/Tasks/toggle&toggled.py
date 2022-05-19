def toggle(var, bunch):
	if var in bunch:
		bunch.discard(var)
	else:
		bunch.add(var)


READ_ONLY = 'read_only'
flags = set()

toggle(READ_ONLY, flags)
print(READ_ONLY in flags)

toggle(READ_ONLY, flags)
print(READ_ONLY in flags)


def toggled(var, bunch):
	new_flags = set()
	if var in bunch:
		new_flags.discard(var)
	else:
		new_flags.add(var)
	return new_flags


READ_ONLY = 'read_only'
flags = set()

new_flags = toggled(READ_ONLY, flags)
print(READ_ONLY in flags)
print(READ_ONLY in new_flags)
