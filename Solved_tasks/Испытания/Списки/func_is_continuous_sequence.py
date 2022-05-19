def is_continuous_sequence(roster):
	if len(roster) > 1:
		for i in range(len(roster) - 1):
			if roster[i + 1] - roster[i] != 1:
				return False
		return True
	return False


print(is_continuous_sequence([10, 11, 12, 13]))
print(is_continuous_sequence([-5, -4, -3]))
print(is_continuous_sequence([10, 11, 12, 14, 15]))
print(is_continuous_sequence([1, 2, 2, 3]))
print(is_continuous_sequence([7]))
print(is_continuous_sequence([]))
