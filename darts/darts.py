import math

r_outer = 10
r_middle = 5
r_inner = 1

def score(x, y):
    distance = math.sqrt(x ** 2 + y ** 2)

    if distance <= r_inner: return 10
    elif distance <= r_middle: return 5
    elif distance <= r_outer: return 1
    else: return 0
