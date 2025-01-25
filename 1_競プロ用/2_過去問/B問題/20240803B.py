from sys import stdin
#------------------整数のリスト-----------------------
def make_intList():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------
#-----------------------------------------------------------------
def make_dict(dict1):
    listDic = dict(enumerate(dict1))
    return listDic
#------------------------------------------------------------------
#------------辞書をvalueでソート------------
def sort_dict_by_values(dict):

    sortedValues = sorted(dict.items(), key=lambda item:item[1], reverse=True) #--False 昇順 True 降順--

    #print(sortedValues)

    sortedDicByValues = {keyTmp: valueTmp for keyTmp, valueTmp in sortedValues}
    return sortedDicByValues
#--------------------------------------------

n = int(input())

inputList = make_intList()

dict1 = make_dict(inputList)

dict1 = sort_dict_by_values(dict1)

keyList = list(dict1.keys())

print(keyList[1]+1)