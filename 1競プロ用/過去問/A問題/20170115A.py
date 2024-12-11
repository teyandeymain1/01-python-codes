from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------

inputList1 = make_intList_func()


area1 = inputList1[0]*inputList1[1]

area2 = inputList1[2]*inputList1[3]

if area1 < area2:
    print(area2)
else:
    print(area1)