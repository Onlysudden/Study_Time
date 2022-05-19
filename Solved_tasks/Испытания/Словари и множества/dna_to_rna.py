def to_rna(dnk):
	rna = ''
	for elem in dnk:
		if elem == 'G':
			rna += 'C'
		elif elem == 'C':
			rna += 'G'
		elif elem == 'T':
			rna += 'A'
		elif elem == 'A':
			rna += 'U'
	return rna


print(to_rna('ACGTGGTCTTAA'))
