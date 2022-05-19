def make_decart_point(x, y):
    return {"x": x, "y": y}


def get_x(point):
    radius = (point["x"] ** 2 + point["y"] ** 2) ** 0.5
    cos = point["x"] / radius
    result = radius * cos
    return result


def get_y(point):
    radius = (point["x"] ** 2 + point["y"] ** 2) ** 0.5
    cos = point["y"] / radius
    result = radius * cos
    return result


x = 4
y = 8

point = make_decart_point(x, y)

print(get_x(point))
print(get_y(point))
