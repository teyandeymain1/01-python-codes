from sys import stdin
#-----------------文字のリスト-----------------------
def make_strList_func():
    readline = stdin.readline
    strList = list(map(str, readline()[:-1]))
    return strList
#------------------------------------------------

inputList1 = make_strList_func()
inputList2 = make_strList_func()

answerList = []

for i in range(len(inputList2)):
    answerList += [inputList1[i]] + [inputList2[i]]
     
if len(inputList2) < len(inputList1):
    answerList += [inputList1[-1]]

print(*answerList, sep = "")