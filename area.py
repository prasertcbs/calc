import math

def rectangle(w, h):
    return w * h

def square(side):
    """calculate square area

    Args:
        side (float): side length

    Returns:
        float: area of square
    """    
    return side ** 2

def triangle(b, h):
    return .5 * b * h

def circle(r):
    return math.pi * r * r


if __name__ == "__main__":
    print(rectangle(5, 4))
    print(triangle(5, 4))
    print(circle(1))