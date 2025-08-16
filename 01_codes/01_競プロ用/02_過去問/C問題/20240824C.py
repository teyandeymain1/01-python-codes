import sys
#------------------整数のタプル-----------------------
def make_int_tuple_list_set():
    readline = sys.stdin.readline
    returnData = list(map(int, readline().split()))
            #↑この部分を list か set に変えることで list か set を作ることができる。
    return returnData
#=====================================================

num = int(input())

inList1 = make_int_tuple_list_set()
 #↑この部分を list か set に変えることで list か set を作ることができる。

count = 0

for i, item in enumerate(inList1):
    count += item//3
    inList1[i] = item%3

print(sum(inList1)+count)