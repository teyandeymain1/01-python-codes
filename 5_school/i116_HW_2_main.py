# 砂川佑太 2510096 s2510096@jaist.ac.jp

from i116_HW_2_functions import *

print("run program inlecture note 2")

# factLoop factRecur
print('n! is calculated.')
s = input('Please input n: ')
n = int(s)
print(n, '! = ', factRecur(n))

# revFactRecu ver 1
print('n! is calculated.')
while True:
    try:
        s = input('Please input n: ')
        n = int(s)
        print(n, '! = ', revFactRecur(n))
        break
    except Exception:
        pass

print('n! is calculated.')
while True:
    try:
        s = input('Please input n: ')
        n = int(s)
        print(n, '! = ', revFactRecur(n))
        break
    except Exception as em:
        print(em)

# srByLinearSearch
print('The square root of ', 200000000, ' is ',
srByLinearSearch(200000000), '.')
print('The square root of ',
20000000000000000, ' is ',
srByLinearSearch(20000000000000000), '.')

# srByBinarySearch
print('The square root of ', 200000000, ' is ',
srByBinarySearch(200000000), '.')
print('The square root of ',
20000000000000000, ' is ',
srByBinarySearch(20000000000000000), '.')

# piWithRectangle
print('pi is ', piWithRectangle(0.001), ', where e is 0.001.')
print('pi is ', piWithRectangle(0.00001), ', where e is 0.00001.')
print('pi is ', piWithRectangle(0.0000001), ', where e is 0.0000001.')

# piWithTrapezoido
print('pi is ', piWithTrapezoido(0.001), ', where e is 0.001.')
print('pi is ', piWithTrapezoido(0.00001), ', where e is 0.00001.')
print('pi is ', piWithTrapezoido(0.0000001), ', where e is 0.0000001.')