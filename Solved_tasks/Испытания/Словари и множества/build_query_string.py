def build_query_string(dict):
	result = []
	for k, v in dict.items():
		result.append(f'{k}={v}')
	return '?' + '&'.join(sorted(result))


dict = {
	'per': 5,
	'page': 7,
	'medium': 'link'
}
print(build_query_string(dict))

dict = {
	'per': 5,
	'medium': 'inst',
	'source': 'bots'
}
print(build_query_string(dict))

dict = {
	'per': 5,
	'page': 1,
	'medium': 'vk',
	'lives': 9
}
print(build_query_string(dict))
