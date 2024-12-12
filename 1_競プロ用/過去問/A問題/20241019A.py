import sys
#------------------整数のタプル-----------------------
readline = sys.stdin.readline
N, C = map(int, readline().replace('\n','').replace('\r','').split())
    #引数が一つの時はここに , を入れること                          #空欄がないときは .split() を消す

inTuple1 = tuple(map(int, readline().replace('\n','').replace('\r','').split()))
                                                                        #空欄がないときは .split() を消す
            #↑この部分を list か set に変えることで list か set を作ることができる。

count = 1
phase = inTuple1[0]

for i in range(N):
    if inTuple1[i] - phase < C:
        continue
    else:
        count += 1
        phase = inTuple1[i]

print(count)