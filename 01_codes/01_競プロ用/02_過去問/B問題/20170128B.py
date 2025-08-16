from sys import stdin
#------------------整数のリスト-----------------------
def make_strList_func():
    readline = stdin.readline
    intList = list(map(str, readline()))
    return intList
#------------------------------------------------

inputList1 = make_strList_func()

for i in range(len(inputList1)):
    if inputList1[i] == "A":
        answerStart = i
        break
for j in range(i, len(inputList1)):
    if inputList1[j] == "Z":
        answerEnd = j

answer = answerEnd - answerStart + 1
    
print(answer)
