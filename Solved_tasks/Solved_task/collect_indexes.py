from collections import defaultdict


def collect_indexes(collect):
	d = defaultdict(list)
	for (index, elem) in enumerate(collect):
		d[elem].append(index)
	return d


d = collect_indexes('hello')

print(d['h'])
print(d['e'])
print(d['l'])
