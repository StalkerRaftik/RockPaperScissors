def print_text(screen, start_x, start_y, text, center=False):
    if center:
        start_x = int(start_x - (len(text) / 2))
    start_x = int(start_x)
    start_y = int(start_y)
    if start_y >= len(screen):
        return
    for i in range(len(text)):
        x = start_x + i
        if x >= len(screen[start_y]):
            return
        screen[start_y][x] = text[i]


def sum_vect(a, b):
    return [x + y for x, y in zip(a, b)]


def get_opposite_vect(a):
    return [-x for x in a]
