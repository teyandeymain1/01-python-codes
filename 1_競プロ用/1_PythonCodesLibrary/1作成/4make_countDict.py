import sys
#-----------------------------------------------------------------
def mk_counter():
    readline = sys.stdin.readline
    _tuple = tuple(map(str, readline().replace('\n','').replace('\r','')))
                                                                        #空欄があるときは .split() をつける
                #↑この部分を list か set に変えることで list か set を作ることができる。
    from collections import Counter    
    return Counter(_tuple) #個数の多い順に並べられる
#=====================================================
xDict = mk_counter()
print(xDict)


import sys
#-----------------------------------------------------------------
def mk_counter():
    #変数定義
    readline = sys.stdin.readline
    _tuple = tuple(map(str, readline().replace('\n','').replace('\r','')))
                                                                        #空欄があるときは .split() をつける
                #↑この部分を list か set に変えることで list か set を作ることができる。
    from collections import defaultdict
    retDict = defaultdict(int)
    #本体
    for key in _tuple:
        retDict[key] += 1 #これだとキーの順序が保証される
    return retDict 
#=====================================================
xDict = mk_counter()
print(xDict)











#=======================getの使い方=======================
import sys
#-----------------------------------------------------------------
def mk_counter_get_ver():
    #変数定義
    readline = sys.stdin.readline
    _tuple = tuple(map(str, readline().replace('\n','').replace('\r','')))
                                                                        #空欄があるときは .split() をつける
                #↑この部分を list か set に変えることで list か set を作ることができる。
    retDict = dict()
    #本体
    for key in _tuple:
        retDict[key] = retDict.get(key, 0) + 1 #これだとキーの順序が保証される
    return retDict
#=====================================================
xDict = mk_counter_get_ver()
print(xDict)