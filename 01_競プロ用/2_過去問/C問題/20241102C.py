import sys

import sys
#------------------整数の行-----------------------
readline = sys.stdin.readline
N, = map(int, readline().replace('\n','').replace('\r','').split())
    #引数が一つの時はここに , を入れること                          #空欄がないときは .split() を消す
#↑ここの , がないと一文字として認識されない。

#------------------整数のタプル-----------------------
readline = sys.stdin.readline
A = list(map(int, readline().replace('\n','').replace('\r','').split()))
                                                                        #空欄がないときは .split() を消す
            #↑この部分を list か set に変えることで list か set を作ることができる。


A.append(-10000000)

searchDict = dict()

buf = []
ansList = []

for i in range(N):
    if A[i] in searchDict:
        ansList.append(searchDict[A[i]]+1)
    else:
        ansList.append(-1)
    
    searchDict[A[i]] = i

print(*ansList)