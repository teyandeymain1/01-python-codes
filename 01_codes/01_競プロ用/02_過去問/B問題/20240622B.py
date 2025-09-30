from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------

valList1 = make_intList_func()

inputList2 = make_intList_func()

count=0

for i in range(valList1[0]*2-2):
    if inputList2[i] == inputList2[i+2]:
        count+=1

print(count)