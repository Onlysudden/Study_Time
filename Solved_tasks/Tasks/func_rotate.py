def rotate(list):
	if list != []:
		list.insert(0, list.pop())


list1 = [1, 2, 3]
list2 = [5, 2, 4]
list3 = [-1, 0, 100]

rotate(list1)
rotate(list2)
rotate(list3)

print(list1, list2, list3, sep='\n')
