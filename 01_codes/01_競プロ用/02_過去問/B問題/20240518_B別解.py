#-----------------------------------------------------------------
def make_dictionary(numOfEle):

    keysList = []
    valuesList = []
    keyTmp = 0
    valueTmp = 0

    for k in range(numOfEle):
        keyTmp, valueTmp = input().split()

         #---intを変更して辞書の要素の型を変更可/keys_listと交換してもよい---       
        keysList.append(str(keyTmp))
        valuesList.append(int(valueTmp))

    listDic = []
    listDic = dict(zip(keysList, valuesList))
    return listDic
#------------------------------------------------------------------
numOfEle = int(input())

listDic1 = make_dictionary(numOfEle)

listDic2 = sorted(listDic1.keys())

x = 0

for y in listDic1.values():
    x = (x + int(y))

z = x % numOfEle

print(listDic2[z])