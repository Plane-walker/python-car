import math


def circle_intersection(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((abs(x2 - x1)) ** 2 + (abs(y2 - y1)) ** 2)
    if d > (r1 + r2) or d < (abs(r1 - r2)):
        return 0, 0
    else:
        a = (r1 ** 2 - r2 ** 2 + d ** 2) / (2 * d)
        h = math.sqrt(r1 ** 2 - a ** 2)
        x_temp = x1 + a * (x2 - x1)/d
        y_temp = y1 + a * (y2 - y1)/d
        x3 = round(x_temp - h * (y2 - y1) / d, 2)
        y3 = round(y_temp + h * (x2 - x1) / d, 2)
        # x4 = round(x_temp + h * (y2 - y1) / d,2)
        # y4 = round(y_temp - h * (x2 - x1) / d,2)
        return x3, y3


def cosine_law(x1, y1, x2, y2, x3, y3):
    dx1 = x2 - x1
    dy1 = y2 - y1
    dx2 = x3 - x1
    dy2 = y3 - y1
    return round(math.acos((dx1 * dx2 + dy1 * dy2) / math.sqrt((dx1 ** 2 + dy1 ** 2) * (dx2 ** 2 + dy2 ** 2))) * 180 / math.pi, 2)
