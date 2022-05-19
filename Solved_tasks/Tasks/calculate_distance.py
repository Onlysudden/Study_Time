def calculate_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    result = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return result


point1 = [0, 0]
point2 = [3, 4]
print(calculate_distance(point1, point2))