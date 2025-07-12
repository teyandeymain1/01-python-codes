from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------
#---------------降順でリストをソート----------------
def sort_list_desc_func(list):
    list = sorted(list, reverse=True) #降順
    return list
#-------------------------------------------------

varList1 = make_intList_func()

inputList1 = make_intList_func()

inputList1 = sort_list_desc_func(inputList1)

inputList1 = inputList1[:(varList1[1])]

print(sum(inputList1))