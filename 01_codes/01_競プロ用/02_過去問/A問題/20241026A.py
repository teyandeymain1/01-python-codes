import sys
#------------------文字のタプル-----------------------
readline = sys.stdin.readline
aTuple = tuple(map(str, readline().replace('\n','').replace('\r','')))
                                                                    #空欄があるときは .split() をつける
            #↑この部分を list か set に変えることで list か set を作ることができる。

if sorted(aTuple) == ['A', 'B', 'C']:
    print("Yes")
else:
    print("No")