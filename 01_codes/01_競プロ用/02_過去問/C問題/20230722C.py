from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------
#------------------内包表記-----------------------
def make_intList_cmprh_ver_func(valList):
    times  = valList
    #-------------以下の"in valList"の部分を書き換える。今回は受け取ったvalListの要素を順に全て新しいリストに代入している-----------------------
    intList = [i for i in range(1, times+1)]
    #---------------ここまで------------------------

    return intList
#------------------------------------------------
#-----------------------------------------------------------------
def make_dictionary_func(valList, inputList):

    numOfEle = valList[0]

    keysList = make_intList_cmprh_ver_func(numOfEle)

    listDic = {}
    listDic = dict(zip(keysList, inputList))
    return listDic
#------------------------------------------------------------------
#------------辞書をkeyでソート------------
def sort_dict_by_keys_func(kwargs):

    sortedKeys = sorted(kwargs, reverse=False) #--False 昇順 True 降順--
    
    sortedDicByKeys = {a: kwargs[a] for a in sortedKeys}
    return sortedDicByKeys
#--------------------------------------------
inputList1 = make_intList_func()

inputList2 = make_intList_func()

inputDic1 = make_dictionary_func(inputList1, inputList2)

print(inputDic1)
