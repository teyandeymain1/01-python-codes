import sys
#-----------------------------------------------------------------
def make_counterDict():
    readline = sys.stdin.readline
    inTuple = tuple(map(str, readline().replace('\n','').replace('\r','')))
                                                                        #空欄があるときは .split() をつける
                #↑この部分を list か set に変えることで list か set を作ることができる。
    from collections import Counter    
    return Counter(inTuple) #個数の多い順に並べられる
#=====================================================
aDict = make_counterDict()
print(aDict)


import sys
#-----------------------------------------------------------------
def make_countDict():
    #変数定義
    readline = sys.stdin.readline
    inTuple = tuple(map(str, readline().replace('\n','').replace('\r','')))
                                                                        #空欄があるときは .split() をつける
                #↑この部分を list か set に変えることで list か set を作ることができる。
    from collections import defaultdict
    retDict = defaultdict(int)
    #本体
    for key in inTuple:
        retDict[key] += 1 #これだとキーの順序が保証される
    return retDict 
#=====================================================
aDict = make_countDict()
print(aDict)


#=======================getの使い方=======================
import sys
#-----------------------------------------------------------------
def make_countDict_get_ver():
    #変数定義
    readline = sys.stdin.readline
    inTuple = tuple(map(str, readline().replace('\n','').replace('\r','')))
                                                                        #空欄があるときは .split() をつける
                #↑この部分を list か set に変えることで list か set を作ることができる。
    retDict = dict()
    #本体
    for key in inTuple:
        retDict[key] = retDict.get(key, 0) + 1 #これだとキーの順序が保証される
    return retDict 
#=====================================================
aDict = make_countDict_get_ver()
print(aDict)