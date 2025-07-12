import sys

#-----------------文字のリスト-----------------------
def make_strList():
    readline = sys.stdin.readline
    strList = list(map(str, readline()[:-1]))
    return strList
import sys
#-----------------------使用済みの数字を記録する集合(列)の作成-------------------------------
def make_colList(varList, inputMatrix):
    #二次元配列を"for rowList"1つで回すと、一行ごとに取得できる。
    colList = [rowList[varList] for rowList  in inputMatrix] 


num = int(input())

inputList1 = []

for i in range(num):
    inputList1.append(make_strList())

lengthMin = 1000000000000000000000000000000000000000000000000000000
lengthmax = 0
addItem = 0
maxLenItem = 0

for i, item in enumerate(inputList1):
    if i == 0:
        continue 
    if len(item) < lengthMin:
        lengthMin = len(item)
        addItem = item
    if len(item) > lengthmax:
        lengthmax = len(item)
        maxLenItem = item

addItem.append("*")
print(addItem)
print(maxLenItem)

inputList1.reverse()

print(inputList1)

answerList = [0]*(len(maxLenItem))

print(answerList)

for i in range(num):
    for j in range(len(maxLenItem)):
        answerList[j] = inputList1[:num][i]
        print(answerList)