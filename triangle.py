def area(a,h):

    """
    Returns area of the triangle

        Input:
            a(float/int) : one side of the triangle
            h(float/int) : altititude drown to that side

        Output:
            triangle_area(float/int) : area of the triangle
    """

    return a*h/2

def perimeter(a,b,c):

    """
    Returns perimeter of the triangle
    
        Input:
            a(float/int) : first side of the triangle
            b(float/int) : second side of the triangle
            c(float/int) : third side of the traingle
    
        Output:
            triangle_perimeter(float/int) : perimeter of the triangle
    """

    sides = sorted([a,b,c])
    if c >= a+b:
        return "Triangle doesn't exists"
    
    return sum(sides)