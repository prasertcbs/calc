def c2f(c: float)->float:
    return c/5*9+32

def f2c(f: float)->float:
    """convert Fahrenheit to Celsius

    Args:
        f (float): degree in Fahrenheit

    Returns:
        [type]: [description]
    """    
    return (f-32)*5/9

if __name__ == "__main__":
    print(c2f(100))
    print(f2c(212))