import sys
import collections
#------------------整数のリスト-----------------------
def make_intList():
    readline = sys.stdin.readline
    intList = list(map(int, readline().split()))
    return intList

#=====================================================

num = int(input())

queryList = [None]*num
ballList = [None]*num

answerDict = collections.defaultdict(int)

for i in range(num):
    inputList1 = make_intList()
    if len(inputList1) == 1:
        query, ball = inputList1[0], -1
    else:
        query, ball = inputList1[0], inputList1[1]
    if query == 1: 
        answerDict[ball] += 1

        #print("answerDict1", answerDict)

    if query == 2:
        answerDict[ball] -= 1
        if answerDict[ball] <= 0:
            answerDict.pop(ball, None)
            #print("answerDict2", answerDict)

    if query == 3:
        #print("aanswerDict3", answerDict)
        print(len(answerDict))