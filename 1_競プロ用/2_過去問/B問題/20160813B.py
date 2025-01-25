from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(str, readline()[:-1]))
    return intList
#------------------------------------------------

inputList1 = make_intList_func()
answerList = []

for i in range(len(inputList1)):
    if len(answerList)>0 and inputList1[i]=="B":
        answerList.pop()
    elif len(answerList)==0 and inputList1[i]=="B":
        continue
    else:
        answerList.append(inputList1[i])

print(*answerList, sep ="")
