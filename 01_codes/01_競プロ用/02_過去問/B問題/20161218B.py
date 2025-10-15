from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------

numOfPrbl = int(input())

inputList1 = make_intList_func()

numOfCan = int(input())

for i in range(numOfCan):
    inputList2 = inputList1.copy()
    inputListTmp = make_intList_func()
    inputList2[(inputListTmp[0]-1)] = inputListTmp[1]
    print(sum(inputList2))