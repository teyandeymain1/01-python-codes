import sys
#------------------文字のタプル-----------------------
readline = sys.stdin.readline
inTuple0 = tuple(map(int, readline().split()))
            #↑この部分を list か set に変えることで list か set を作ることができる。
            #空欄があるときは .split() を使う
inTuple1 = tuple(map(int, readline().split()))
            #↑この部分を list か set に変えることで list か set を作ることができる。
            #空欄があるときは .split() を使う
inTuple2 = tuple(map(int, readline().split()))
            #↑この部分を list か set に変えることで list か set を作ることができる。
            #空欄があるときは .split() を使う

inTuple1 = sorted(inTuple1)
inTuple2 = sorted(inTuple2)

print(inTuple1[-1]+inTuple2[-1])