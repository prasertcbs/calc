import math

def cubic(side):
    """[summary]

    Args:
        side ([type]): [description]

    Returns:
        [type]: [description]
    """    
    return side ** 3

def cylinder(radius, height):
    """[summary]

    Args:
        r ([type]): [description]
        h ([type]): [description]

    Returns:
        [type]: [description]
    """    
    return math.pi * (radius ** 2) * height
    