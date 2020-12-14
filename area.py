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
    """[summary]

    Args:
        b ([type]): [description]
        h ([type]): [description]

    Returns:
        [type]: [description]
    """    
    return .5 * b * h

def circle(r):
    """[summary]

    Args:
        r ([type]): [description]

    Returns:
        [type]: [description]
    """    
    return math.pi * r * r

def ellipse(a, b):
    """ellipse area

    Args:
        a ([type]): [description]
        b ([type]): [description]

    Returns:
        [type]: [description]
    """    
    return math.pi * a * b

if __name__ == "__main__":
    print(rectangle(5, 4))
    print(triangle(5, 4))
    print(circle(1))