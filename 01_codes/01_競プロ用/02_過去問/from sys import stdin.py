from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------
from collections import deque
#------------------リストの回転-----------------------
def rotate_list_func(valList, inputList):
    start = valList

    inputList = deque(inputList)

    inputList.rotate(-start) #右回転は+、左回転は-
    return list(inputList)
#------------------------------------------------

num = int(input())

nameList1 = [0]*num
intList1 = [0]*num

for i in range(num):
    readline = stdin.readline
    nameList1[i], intList1[i] = list(map(str, readline().split()))

intList1 = list(map(int, intList1))

resultTmp = 1000000000000000000000000000000000000000000000000000000000000000000000000000

for j in range(len(intList1)):
    if intList1[j] <= resultTmp:
        result = j
        resultTmp = intList1[j]
        
answerList = rotate_list_func(result, nameList1)

print(*answerList, sep="\n")