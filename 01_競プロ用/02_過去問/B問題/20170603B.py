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

def compare_neighbor_in_list_func(rcrsVar, varList, inputList):

    #-----------以下に操作に必要な変数を書く--------------
    answer = "no"
    contNumTmp = 0
    #----------------ここまで------------------------
    inputList = inputList + ["?"]


    for i in range(len(inputList) - 1):
        if 0 == 0 and not inputList[i] == inputList[i+1]:
            contNumTmp += 1 #0を見つけた回数を記録
        else:
            continue

    
    if contNumTmp == (len(inputList) - 1):
        answer = "yes"

    return answer
#--------------------------------------------------------------------

inputList1 = make_strList_func()

inputList1 = sort_list_asc_func(inputList1)

#---------関数内に追加したい変数を配列の最後に追加------------- 
#----------------------ここまで-----------------------------

print(compare_neighbor_in_list_func(0, 0, inputList1))
