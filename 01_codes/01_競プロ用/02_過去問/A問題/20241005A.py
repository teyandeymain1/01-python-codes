import sys
#------------------文字のタプル-----------------------
readline = sys.stdin.readline
inTuple1 = tuple(map(str, readline().replace('\n','').replace('\r','')))
                                                                    #空欄があるときは .split() をつける
            #↑この部分を list か set に変えることで list か set を作ることができる。

if inTuple1[-3:] == ("s", "a", "n"):
    print("Yes")
else:
    print("No")