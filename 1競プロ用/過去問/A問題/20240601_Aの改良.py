#------------------整数のリスト-----------------------
def make_intList_func():
    intList = list(map(int, input().split()))
    return intList
#------------------------------------------------
#---------------降順でリストをソート----------------
def sort_list_desc_func(list):
    list = sorted(list, reverse=True) #降順
    return list
#-------------------------------------------------

list1 = make_intList_func()

list2 = [i for i in range(1, (list1[0]+1))]

sliceStart = list1[1] - 1
sliceEnd = list1[2]

listSlice = list2[sliceStart:sliceEnd]
listSlice2 = sort_list_desc_func(listSlice)

list2[sliceStart:sliceEnd] = listSlice2[0:len(listSlice2)]

print(*list2)