from sys import stdin
#-----------------文字のリスト-----------------------
def make_strList_func():
    readline = stdin.readline
    strList = list(map(str, readline()[:-1]))
    return strList
#------------------------------------------------
inputList3 = make_strList_func()
inputSet = set(inputList3)

answerList = []
answer = "No"

for i in range(len(inputSet)):
    count = 0
    for j in range(len(inputList3)):
        if inputList3[j] == list(inputSet)[i]:
            count += 1
    if count%2 == 0:
        answerList.append("Yes")
if len(answerList) == len(inputSet):
    answer = "Yes"

print(answer)