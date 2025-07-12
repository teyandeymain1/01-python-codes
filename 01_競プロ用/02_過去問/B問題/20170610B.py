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

varNum = int(input()) - 1

inputList1 = make_intList_func()

startP = inputList1[varNum]

inputList1 = list(set(inputList1))
inputList1 = sort_list_asc_func(inputList1)

print(inputList1[-1] - inputList1[0])