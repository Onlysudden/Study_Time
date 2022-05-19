def rotated_left(list):
	return list[1:] + list[0:1]


def rotated_right(list):
	return list[-1:] + list[:-1]


text1 = [1, 2, 3]
text2 = "dakar"
text3 = (5, 'da', -5, 4)

print(rotated_left(text1))
print(rotated_left(text2))
print(rotated_left(text3))

print(rotated_right(text1))
print(rotated_right(text2))
print(rotated_right(text3))
