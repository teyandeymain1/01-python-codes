import sys
#------------------整数のリスト-----------------------
def make_str_list():
    readline = sys.stdin.readline
    return list(map(str, readline()[:-1]))
            #↑この部分を list か set に変えることで list か set を作ることができる。
#------------辞書をvalueでソート------------
def sort_dict_by_values(dict):
    #item()で辞書からkey, valueをタプル(key, value)で出してvalue(item[1])でソート。
    sortedValues = sorted(dict.items(), key=lambda item:item[1], reverse=True) #--False 昇順 True 降順--
    #print(sortedValues)
    return {keyBuf: valueBuf for keyBuf, valueBuf in sortedValues}
#---------------------------------- 行列を表示する---------------------------------------
def print_matrix(inMatrix):
    for rowList in inMatrix:         
        print("".join(map(str, rowList)))
#=========================================main=========================================
def main():

    inList = make_str_list()
    ansList = make_str_list()    

    ansMatrix = []

    for i in range(len(inList)):
        if inList[i] > ansList[i]:
            inList[i] = ansList[i]
            ansMatrix.append(inList[:])

    for j in range((len(inList)-1), -1, -1):
        if inList[j] != ansList[j]:
            inList[j] = ansList[j]
            ansMatrix.append(inList[:]) 
                   
    print(len(ansMatrix))
    print_matrix(ansMatrix)

if __name__ == "__main__": 
    main()