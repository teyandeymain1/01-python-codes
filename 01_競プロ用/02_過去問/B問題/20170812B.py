from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------

inputList1 = make_intList_func()

minMinute1 = max(inputList1[0], inputList1[2])
maxMinute1 = min(inputList1[1], inputList1[3])

answer = 0

if (maxMinute1 - minMinute1) < 0:
    print(answer)
else:
    answer = (maxMinute1 - minMinute1)
    print(answer)