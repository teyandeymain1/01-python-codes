#----------------------------------------------
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
#リストA
list2 = make_intList_func()
#リストB
list3 = make_intList_func()

#合計
list4 = list2 + list3

list2 = sort_list_asc_func(list2)
list3 = sort_list_asc_func(list3)
list4 = sort_list_asc_func(list4)

lista = [1000000000000000000000000000000000]
listb = [2000000000000000000000000000000000]

list2a = list2 + lista
list4b = list4 +listb

answer = "No"

if len(list2) == 1:
    answer = "No"
else:
    for i in range(len(list4)):
        for j in range(len(list2)):
            if list2a[j] == list4b[i] and list2a[j + 1] == list4b[i + 1]:
                answer = "Yes"
            else:
                continue
                
print(answer)