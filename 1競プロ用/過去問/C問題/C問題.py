from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------
inputList1 = make_intList_func()
list1 = make_intList_func()

n = inputList1[0]
a = inputList1[1]

