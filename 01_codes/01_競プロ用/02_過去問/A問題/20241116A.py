import sys
#-----------------------------------------------------------------
def make_counterDict():
    readline = sys.stdin.readline
    inTuple = tuple(map(int, readline().replace('\n','').replace('\r','')))
                                                                        #空欄があるときは .split() をつける
                #↑この部分を list か set に変えることで list か set を作ることができる。
    from collections import Counter    
    return Counter(inTuple) #個数の多い順に並べられる
#=====================================================
aDict = make_counterDict()

if aDict[1] == 1 and aDict[2] == 2 and aDict[3] == 3:
    print("Yes")
else:
    print("No")

