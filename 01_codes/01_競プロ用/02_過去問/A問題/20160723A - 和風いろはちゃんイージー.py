#------------------整数のリスト-----------------------
def make_intList_func():
    intList = list(map(int, input().split()))
    return intList
#------------------------------------------------
#---------------昇順でリストをソート---------------
def sort_list_asc_func(list):
    list = sorted(list, reverse=False) #昇順
    return list
#-------------------------------------------------

list1 = make_intList_func()
list1 = sort_list_asc_func(list1)

answer = "NO"

if list1 == [5, 5, 7]:
    answer = "YES"

print(answer)