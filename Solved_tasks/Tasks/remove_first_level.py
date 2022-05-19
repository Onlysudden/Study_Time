def remove_first_level(tree):
    result = []
    for elem in tree:
        if isinstance(elem, int) is False:
            for m in elem:
                result.append(m)
    return result


tree1 = [[5], 1, [3, 4]]
print(remove_first_level(tree1))

tree2 = [1, 2, [3, 5], [[4, 3], 2]]
print(remove_first_level(tree2))
