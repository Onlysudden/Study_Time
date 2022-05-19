def same_parity_filter(book):
    s = []
    if book == []:
        return book
    if book[0] % 2 == 0:
        for elem in book:
            if elem % 2 == 0:
                s.append(elem)
    else:
        for elem in book:
            if elem % 2 != 0:
                s.append(elem)
    return s


print(same_parity_filter([]))
print(same_parity_filter([2, 0, 1, -3, 10, -2]))
print(same_parity_filter([-1, 0, 1, -3, 10, -2]))
