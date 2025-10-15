from sys import stdin
#------------------小数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------

inputList1=make_intList_func()

inputList2=make_intList_func()

answer=abs(inputList1[1]-inputList2[1])


if abs(inputList1[0]-inputList2[0]) > abs(inputList1[1]-inputList2[1]):
    answer+=1

print(answer)