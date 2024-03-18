def equilateral(sides):
    a, b, c = sides
    return triangle(sides) and a == b and b == c and a == c


def isosceles(sides):
    a, b, c = sides
    return triangle(sides) and (a == b or b == c or a == c)


def scalene(sides):
    return triangle(sides) and not equilateral(sides) and not isosceles(sides)


def triangle(sides):
    a, b, c = sides
    return all(sides) and not (a + b < c or b + c < a or a + c < b)
