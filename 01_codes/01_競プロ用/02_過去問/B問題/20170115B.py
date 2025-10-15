from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------
#-----------------文字のリスト-----------------------
def make_strList_func():
    readline = stdin.readline
    strList = list(map(str, readline()[:-1]))
    return strList
#------------------------------------------------

inputList1 = make_intList_func()
inputList2 = make_strList_func()

answerList = []
answerTmp = 0
answer = 0

for i in inputList2:
    if i == "I":
        answerList = answerList + [1]
    elif i == "D":
        answerList = answerList + [-1]
    
    if answerTmp < sum(answerList):
        answer = sum(answerList)
        answerTmp = sum(answerList)

print(answer)