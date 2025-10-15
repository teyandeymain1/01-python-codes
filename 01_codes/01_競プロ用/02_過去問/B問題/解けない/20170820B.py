from sys import stdin
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

inputList1 = make_strList_func()
inputList1 = list(set(inputList1))

answer = "None"

compareList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for item in compareList:
    if item not in inputList1:
        answer = item
        break

print(answer)