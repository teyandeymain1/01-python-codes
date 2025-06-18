
# formula of quarter circle
def f(x):
    return (4 - x**2)**(1/2)

# area of rectangle
def h(i,n):
    return f(i*(2/n)) * (2/n)

# area of trapezoid
def g(i,n):
    return (f(i*(2/n)) + f((i+1)*(2/n))) * (2/n) * (1/2)

def piWithRectangle(e):
    n = 1
    v1 = 0
    v2 = e+1
    while abs(v1 - v2) > e:
        n = 2 * n
        v1 = v2
        v2 = 0
        for i in range(n):
            v2 = v2 + h(i,n)
    return v2

def piWithTrapezoido(e):
    n = 1
    v1 = 0
    v2 = e+1
    while abs(v1 - v2) > e:
        n = 2 * n
        v1 = v2
        v2 = 0
        for i in range(n):
            v2 = v2 + g(i,n)
    return v2