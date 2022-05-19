def make_rectangle(x, y, width, height):
    return {
        "x": x, "y": y,
        "width": width,
        "height": height
    }


def get_start_point(rectangle):
    result = []
    result.append(rectangle['x'])
    result.append(rectangle['y'])
    return result


def get_width(rectangle):
    result = rectangle['width']
    return result


def get_height(rectangle):
    result = rectangle['height']
    return result


def contains_origin(x, y, rectangle):
    if (rectangle['x'] >= x
            and x >= rectangle['x'] - get_height(rectangle)
            and rectangle['y'] <= y
            and y <= rectangle['y'] + get_width(rectangle)):
        return 'Yes!'
    else:
        return 'No!'


x = 5
y = 2
width = 3
height = 4

start_point = make_rectangle(x, y, width, height)

print(get_start_point(start_point))
print(get_width(start_point))
print(get_height(start_point))
print(contains_origin(3, 3, start_point))
print(contains_origin(1, 1, start_point))
