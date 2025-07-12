from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------
#-----------------------------------------------------------------
def make_dictionary_keys_free_ver_func(varList):
    readline = stdin.readline

    numOfEle = varList

    keysList = [0] * numOfEle
    valuesList = [0] * numOfEle

    for k in range(numOfEle):
        keyTmp, valueTmp = readline().split()

         #---intを変更して辞書の要素の型を変更可/keys_listと交換してもよい---       
        keysList[k] = str(keyTmp)
        valuesList[k] = int(valueTmp)

    listDic = {}
    listDic = dict(zip(keysList, valuesList))
    return listDic
#------------------------------------------------------------------
#------------辞書をkeyでソート------------
def sort_dict_by_keys_func(kwargs):

    sortedKeys = sorted(kwargs, reverse=False) #--False 昇順 True 降順--
    
    sortedDicByKeys = {a: kwargs[a] for a in sortedKeys}
    return sortedDicByKeys
#--------------------------------------------
readline = stdin.readline
N = int(readline()[:-1])

inputDic1 = make_dictionary_keys_free_ver_func(N)

inputDic2 = sort_dict_by_keys_func(inputDic1)



keyList = list(inputDic2.keys())

answer = int(keyList[-1])

if inputDic2[keyList[-1]] >= 0:

    answer += inputDic2[keyList[-1]]



print(answer)