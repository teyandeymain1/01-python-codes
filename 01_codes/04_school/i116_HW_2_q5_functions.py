# 砂川佑太 2510096 s2510096@jaist.ac.jp
# Homework q5

# formula of quarter circle
def f(x):
    return (1-(x-1)**2)**(0.5)

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
            v2 = v2 + h(i,n) * 2
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
            v2 = v2 + g(i,n) * 2
    return v2

import time
def stopwatch(func_name, func, e):
    start = time.time()
    if func_name == "piWithRectangle":
        result = piWithRectangle(e)
    elif func_name == "piWithTrapezoido":
        result = piWithTrapezoido(e)
    else:
        raise Exception("Unknown function name") # エラー発生時の文はchatGPTに生成させました
    end = time.time()
    time_diff = end - start
    print(f"Elapsed time for {func_name}({e}) is {time_diff:.6f} seconds") # この文の一部はchatGPTに生成させました
    return None