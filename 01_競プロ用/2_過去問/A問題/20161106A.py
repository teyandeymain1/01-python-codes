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

inputList1 = make_intList_func()

inputList1 = sort_list_asc_func(inputList1)

sumCan = 0
answer = "No"

sumCan = inputList1[0] + inputList1[1]

if sumCan == inputList1[2]:
    answer = "Yes"

print(answer)