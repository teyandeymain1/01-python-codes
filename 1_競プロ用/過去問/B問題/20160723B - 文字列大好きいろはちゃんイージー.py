#------------------整数のリスト-----------------------
def make_intList_func():
    intList = list(map(int, input().split()))
    return intList
#------------------------------------------------
#----------------------------------------------
def make_strList_func():
    strList = list(map(str, input()))
    return strList
#------------------------------------------------
#---------------昇順でリストをソート---------------
def sort_list_asc_func(list):
    list = sorted(list, reverse=False) #昇順
    return list
#-------------------------------------------------

listInput = make_intList_func()

list1 = []

for i in range(listInput[0]):
    strRow = str(input())
    list1.append(strRow)
    list1 = sort_list_asc_func(list1)

list1 = "".join(list1)
print(list1)