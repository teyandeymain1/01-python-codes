import sys
#------------------------(str)辞書の作成(str)--------------------------------
def mk_dict(num):
    #変数定義
    readline = sys.stdin.readline
    #入力の読み込み
    _tuple = tuple(tuple(map(str, readline().replace('\n','').replace('\r','').split())) for _ in [None]*num)
                                                                                #空欄がないときは .split() を消す
                    #↑この部分を list か set に変えることで list か set を作ることができる。
    #keyとvalueの分離して辞書に登録
    return dict((rowList[0], rowList[1]) for rowList in _tuple) #rowList[0]とrowList[1]を交換するとkeyとvalueが逆転する
#=====================================================


import sys
#------------------------(int)辞書の作成(int)--------------------------------
def mk_dict(num):
    #変数定義
    readline = sys.stdin.readline
    #入力の読み込み
    _tuple = tuple(tuple(map(int, readline().replace('\n','').replace('\r','').split())) for _ in [None]*num)
                                                                                #空欄がないときは .split() を消す
                    #↑この部分を list か set に変えることで list か set を作ることができる。
    #keyとvalueの分離して辞書に登録
    return dict((rowList[0], rowList[1]) for rowList in _tuple) #rowList[0]とrowList[1]を交換するとkeyとvalueが逆転する
#=====================================================

readline = sys.stdin.readline
n, = map(int, readline().replace('\n','').replace('\r','').split())
    #引数が一つの時はここに , を入れること                          #空欄がないときは .split() を消す
xDict = mk_dict(n)
print(xDict)
