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
inputList1 = inputList1[:-1]

flag = "down"

while flag == "down":

    inputList2 = inputList1

    print(inputList2[0:(len(inputList2)//2)])
    print(inputList2[len(inputList2)//2:])
    
    if inputList2[:(len(inputList2)//2)] == inputList2[len(inputList2)//2:]:
        flag = "up"
    else:
        inputList1 = inputList1[:-1]

print(len(inputList1))