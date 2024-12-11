import sys
#-----------------------------------------------------------------
def make_counterDict():
    readline = sys.stdin.readline
    inTuple = tuple(map(str, readline().replace('\n','').replace('\r','').split()))
                                                                        #空欄があるときは .split() をつける
                #↑この部分を list か set に変えることで list か set を作ることができる。
    from collections import Counter    
    return Counter(inTuple) #個数の多い順に並べられる
#=====================================================
aDict = make_counterDict()



ans = 0
for i in list(aDict):
    if int(aDict[i]) == 1:
        continue
    else:
        ans += int(aDict[i])//2

print(ans)
