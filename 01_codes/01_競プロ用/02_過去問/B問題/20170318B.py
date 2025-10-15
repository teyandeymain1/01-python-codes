from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------

intList1 = make_intList_func()

if intList1[1] <= intList1[2] and (intList1[0]+intList1[1]) >= intList1[2]:
    answer = 0
elif intList1[1] < intList1[2] and (intList1[0]+intList1[1]) < intList1[2]:
    answer = intList1[2] - (intList1[0]+intList1[1])
elif intList1[1] >= intList1[2] and (intList1[0]+intList1[2]) >= intList1[1]:
    answer = 0
elif intList1[1] > intList1[2] and (intList1[0]+intList1[2]) < intList1[1]:
    answer = intList1[1] - (intList1[0]+intList1[2])

print(abs(answer))