from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------

varList1 = make_intList_func()

inputList1 = make_intList_func()

inputList1.insert((varList1[1]), varList1[2])

print(*inputList1, sep=" ")