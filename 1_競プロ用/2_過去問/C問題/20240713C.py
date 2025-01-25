
from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------

numOfInput = int(input())

possibleNumList = []

for i in [0]*numOfInput:
    inputList1 = make_intList_func()
    possibleNumList += [list(range((inputList1[0]), (inputList1[1]+1), 1))]

print(possibleNumList)

answerList = [10**9+1]*numOfInput 
flag = "dawn"

while flag == "dawn":
    for j in range(numOfInput):
        answerList = []
        for k in range(len(possibleNumList[j])):
            answerList += [possibleNumList[j][k]]
    print(answerList)
    if sum(answerList) == 0:
        print("Yes")
        print(*answerList)
else:
    print("No")