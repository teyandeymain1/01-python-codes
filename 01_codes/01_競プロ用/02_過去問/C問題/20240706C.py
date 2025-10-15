from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------
#---------------昇順でリストをソート---------------
def sort_list_asc_func(list):
    list = sorted(list, reverse=False) #昇順
    return list
#-------------------------------------------------

varList = make_intList_func()
numOfLeft = varList[0] - varList[1]
inputList1 = make_intList_func()
inputList1 = sort_list_asc_func(inputList1)

print(inputList1)
print(numOfLeft)

answerTmp = 1000000000000000000000000000000
answer = 0

for i in range(0, varList[1]+1):

    print("C: " + str(inputList1[numOfLeft+i-1]))
    print("D: " + str(inputList1[i]))

    if (inputList1[numOfLeft+i-1] - inputList1[i]) < answerTmp:
        answerTmp = (inputList1[numOfLeft+i-1] - inputList1[i])
        answer = (inputList1[numOfLeft+i-1] - inputList1[i])

        print(answer)

    else:
        continue

print(answer)