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
    return dict((rowList[0], rowList[1]) for rowList in inTuple) #rowList[0]とrowList[1]を交換するとkeyとvalueが逆転する
#=====================================================
readline = sys.stdin.readline
nmOfEl, = map(int, readline().replace('\n','').replace('\r','').split())
    #引数が一つの時はここに , を入れること                          #空欄がないときは .split() を消す
aDict = make_dict_freeKeys(nmOfEl)
print(aDict)