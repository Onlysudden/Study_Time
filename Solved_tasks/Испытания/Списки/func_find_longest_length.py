def find_longest_length(stroka):
	max_count = 0
	for i in range(len(stroka) - 1):
		if max_count < len(stroka[i:]):
			if stroka.count(stroka[i], i + 1) >= 1:
				j = stroka.find(stroka[i], i + 1)
				one_count = len(stroka[i:j])
				two_count = len(stroka[j:])
				if max_count < one_count or max_count < two_count:
					max_count = max(one_count, two_count)
			else:
				third_count = len(stroka[i:])
				if max_count < third_count:
					max_count = third_count
	return max_count


print(find_longest_length('qweqrty'))
print(find_longest_length('wassap'))
print(find_longest_length('qweqruywsh'))
print(find_longest_length('qweqwtye'))
