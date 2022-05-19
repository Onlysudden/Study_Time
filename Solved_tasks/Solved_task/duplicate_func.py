def duplicate(list):
	a = []
	a += list
	for i in range(len(list)):
		list.append(a[i])


numbers = [1, 2, 3]
numbers2 = [4, 5, 2]
numbers3 = [4, 7, 8, 12, 0]

duplicate(numbers)
duplicate(numbers2)
duplicate(numbers3)

print(numbers)
print(numbers2)
print(numbers3)
