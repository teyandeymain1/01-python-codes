# 砂川佑太 2510096 s2510096@jaist.ac.jp

def factLoop(n):
    redBox = 1
    blueBox = 1
    while blueBox < n or blueBox == n:
        redBox = redBox * blueBox
        blueBox = blueBox + 1
    return redBox

def factRecur(n):
    if n == 0:
        return 1
    else:
        return n * factRecur(n-1)

def revFactRecur(n):
    if n < 0:
        raise Exception('The argument must be a natural number, such as 0, 1 and 2!')
    elif n == 0:
        return 1
    else:
        return n * revFactRecur(n-1)

# find the square root of v0
def srByLinearSearch(v0):
    for i in range(v0):
        if i * i > v0:
            return i - 1

def srByBinarySearch(v0):
    v1 = 0
    v2 = v0
    while v1 != v2:
        if (v2-v1)%2 == 0:
            v3 = v1+(v2-v1)//2
        else:
            v3 = v1+(v2-v1)//2+1
        if v3*v3 > v0:
            v2 = v3-1
        else:
            v1 = v3
    return v1

# calulate pi

# formula of quarter circle
def f(x):
    return (4 - x**2)**(1/2)

# area of rectangle
def h(i,n):
    return f(i*(2/n)) * (2/n)]

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

