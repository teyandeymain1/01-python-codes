import numpy as np

#------------------整数のリスト-----------------------
def make_intList_func():
    intList = list(map(int, input().split()))
    return intList
#------------------------------------------------

list1 = make_intList_func()
list2 = make_intList_func()

row = list1[0]
col = list1[1]

cookieCoordinate = np.zeros((row, col),dtype=int)

for i in range(row):
    cookieCoordinate[i] = make_intList_func()

answerCount = 0
sumRowList = list(np.sum(cookieCoordinate, axis=0))

for i in range(len(list2)): 
    if sumRowList[i] >= list2[i]:
        answerCount += 1
    else:
        continue

answer = "No"
if answerCount == len(list2):
    answer = "Yes"

print(answer)