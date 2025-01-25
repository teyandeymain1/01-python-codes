import sys
#---------------------------辞書の作成----------------------------------
def make_dict_freeKeys(nmOfEl):
    #変数定義   
    readline = sys.stdin.readline
    #入力の読み込み
    inTuple = tuple(tuple(map(int, readline().replace('\n','').replace('\r','').split())) for _ in [None]*nmOfEl)
                                                                                #空欄がないときは .split() を消す
                              #↑この部分の int を str にして辞書の要素の型を変更可
                    #↑この部分を list か set に変えることで list か set を作ることができる。
    #keyとvalueの分離して辞書に登録
    return dict((rowList[0], int(rowList[1])) for rowList in inTuple) #rowList[0]とrowList[1]を交換するとkeyとvalueが逆転する
#------------辞書をkeyでソート------------
def sort_dict_by_keys(inDict):
    keysList = list(inDict)
    sortedKeys = sort_by_merge(keysList) #マージソート
    #print(sortedValues)    
    return dict((key, inDict[key]) for key in sortedKeys)
#-------------------マージソート-------------------------
def sort_by_merge(inList):
    print("inList", inList)
    if len(inList) <= 1:
        return inList
    else:
        mid = len(inList)//2 #半分の位置を計算
        print("左", inList[:mid], "右",inList[mid:])         
               #再帰的に分割&統合    #左側を分割                   #右側を分割
        return merge(sort_by_merge(inList[:mid]), sort_by_merge(inList[mid:])) 
#合併
def merge(leftList, rightList):
    #変数定義
    sortedList = []
    left, right = 0, 0
    #
    while (left < len(leftList)) and (right < len(rightList)):
        if leftList[left] <= rightList[right]:  #左<=右のとき
            sortedList.append(leftList[left])   #左側から1つ取り出してsortedListに追加
            left += 1
        else:
            sortedList.append(rightList[right]) #右側から1つ取り出してsortedListに追加
            right += 1
        print("sortedList", sortedList)
    # 残りをまとめて追加
    if left < len(leftList):
        sortedList.extend(leftList[left:])   #左側の残りを追加
    if right < len(rightList):
        sortedList.extend(rightList[right:]) #右側の残りを追加
    print("残りをまとめて追加 sortedList", sortedList)
    return sortedList
#-----------マージソート終わり-------------

readline = sys.stdin.readline
nmOfEl, = map(int, readline().replace('\n','').replace('\r','').split())
    #引数が一つの時はここに , を入れること                          #空欄がないときは .split() を消す
inDic1 = make_dict_freeKeys(nmOfEl)

inDic2 = sort_dict_by_keys(inDic1)

print(inDic1)
print(inDic2)