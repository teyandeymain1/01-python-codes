import sys
#------------------------辞書の作成--------------------------------
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
#-----------------------------------辞書をkeyでソート-------------------------------------
def sort_dict_by_keys(inDict):
    sortedKeys = sorted(inDict, reverse=False) # False 昇順 True 降順、sorted内で辞書の名前(inDict)だけ書くとkeyがリストになる。
    return dict((key, inDict[key]) for key in sortedKeys)
#=====================================================
readline = sys.stdin.readline
nmOfEl, = map(int, readline().replace('\n','').replace('\r','').split())
    #引数が一つの時はここに , を入れること                          #空欄がないときは .split() を消す
aDict = make_dict_freeKeys(nmOfEl)
bDict = sort_dict_by_keys(aDict)

print(aDict)
print(bDict)

""""
8
3 4
2 6
0 1
5 3
7 0
1 7
6 2
4 5
"""