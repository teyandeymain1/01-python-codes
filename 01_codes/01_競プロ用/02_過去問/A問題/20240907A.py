import sys
#------------------整数のタプル-----------------------
def make_int_tuple_list_set():
    readline = sys.stdin.readline
    return tuple(map(int, readline().split()))
            #↑この部分を list か set に変えることで list か set を作ることができる。
#=====================================================

inTuple1 = make_int_tuple_list_set()
 #↑この部分を list か set に変えることで list か set を作ることができる。

L, R = inTuple1

if L == 1 and R == 0:
    print("Yes")
elif L == 0 and R == 1:
    print("No")
else:
    print("Invalid")