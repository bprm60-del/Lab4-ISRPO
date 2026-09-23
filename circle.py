import math


def area(r):

    """
    Returns area of the circle with radius = r

        Input:
            r(float/int) : radius

        Output:
            circle_area(float/int) : area of the circle
    """
    return math.pi * r * r


def perimeter(r):

    """
    Returns perimeter of the circle with radius = r
    
        Input:
            r(float/int) : radius
    
        Output:
            circle_perimeter(float/int) : perimeter of the circle
    """
    
    return 2 * math.pi * r