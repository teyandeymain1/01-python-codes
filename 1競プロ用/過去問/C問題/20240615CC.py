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
#---------------昇順でリストをソート---------------
def sort_list_asc_func(list):
    list = sorted(list, reverse=False) #昇順
    return list
#-------------------------------------------------

inputList1 = make_intList_func()

N = inputList1[0]
M = inputList1[1]

resultList = make_strList_func()
answerList = ["x"] * M
for i in range(M):
    answerList[i] = "o"
print(answerList)

count = 0

for i in range(N):
    tmpList = make_strList_func()

    for j in range(M):
        if tmpList[j] == "o":
            resultList[j] =  tmpList[j]
    count += 1
    print(sort_list_asc_func(resultList))
    if sort_list_asc_func(resultList) == answerList:
        break
print(count)
