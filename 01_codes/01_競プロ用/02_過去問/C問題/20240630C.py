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

numInt = int(input())

inputList1 = make_intList_func()
inputList2 = make_intList_func()

sortList1 = sort_list_asc_func(inputList1)

dabuList = []

for i in range(len(sortList1)-1):
    if sortList1[i] == sortList1[i+1]:
        dabuList += [sortList1[i]]
        dabuList = list(set(dabuList))

dabuWeightList = []
repeat = 0

for j in range(len(dabuList)):
    for k in range(len(inputList1)):
        if inputList1[k] == dabuList[j]:
            dabuWeightList += [inputList2[k]]

print(dabuWeightList)