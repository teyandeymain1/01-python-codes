import sys
#------------------整数のリスト-----------------------
def make_strList():
    readline = sys.stdin.readline
    strList = list(map(str, readline()[:-1]))
    return strList
#=====================================================

inputList1 = make_strList()
inputList1.reverse()

ansSlice = 0
for i, item in enumerate(inputList1):
    if item == "0": 
        ansSlice = i
    elif item == ".":
        ansSlice = i+1
        break
    else:
        ansSlice = i
        break
answerList = inputList1[ansSlice:]
answerList.reverse()

print(*answerList, sep="")