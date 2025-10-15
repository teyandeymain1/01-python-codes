from sys import stdin
#------------------整数の集合-----------------------
def make_intSet_func():
    readline = stdin.readline
    intSet = set(map(int, readline().split()))
    return intSet
#------------------------------------------------

inputSet1 = make_intSet_func()

print(len(inputSet1))