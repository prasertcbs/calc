def rectangle(w, h):
    return w * h

def triangle(b, h):
    return .5 * b * h

def circle(r):
    return 22 / 7 * r * r


if __name__ == "__main__":
    print(rectangle(5, 4))
    print(triangle(5, 4))
    print(circle(1))