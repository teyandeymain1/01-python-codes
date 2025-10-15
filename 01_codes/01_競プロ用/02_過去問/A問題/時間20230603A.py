from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
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

answerList = nameList1[(result):num] + nameList1[0:(result)]

print(*answerList, sep="\n")