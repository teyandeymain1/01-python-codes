from sys import stdin
#-----------------文字のリスト-----------------------
def make_strList_func():
    readline = stdin.readline
    strList = list(map(str, readline()[:-1]))
    return strList
#------------------------------------------------

inputList3 = make_strList_func()

answerList = []

for i in inputList3:
    if i == "B" and not len(answerList) == 0:
        answerList = answerList[:-1]
    elif  i == "B" and len(answerList) == 0:
        continue
    else:
        answerList.append(i)
        

print(*answerList, sep = "")