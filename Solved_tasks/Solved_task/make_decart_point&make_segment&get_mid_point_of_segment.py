def make_decart_point(x, y):
    return {"x": x, "y": y}


def make_segment(p1, p2):
    result = {"x1": p1["x"], "y1": p1["y"], "x2": p2["x"], "y2": p2["y"]}
    return result


def get_mid_point_of_segment(line):
    return {
        'x': (line['x1'] + line['x2']) / 2,
        'y': (line['y1'] + line['y2']) / 2}


segment = make_segment(make_decart_point(3, 2), make_decart_point(5, 3))
print(get_mid_point_of_segment(segment))
