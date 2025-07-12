import sys
#------------------整数のタプル-----------------------
def make_int_tuple_list_set():
    readline = sys.stdin.readline
    returnData = list(map(int, readline().split()))
            #↑この部分を list か set に変えることで list か set を作ることができる。
    return returnData
#---------------降順でリストをソート----------------
def sort_list_desc(inList):
    inList = sorted(inList, reverse=True) #降順
    return inList
#=====================================================

inList1 = make_int_tuple_list_set()
 #↑この部分を list か set に変えることで list か set を作ることができる。

inList2 = make_int_tuple_list_set()

count = 0
while True:
    listmax1st = max(inList2)
    inList2.remove(listmax1st)
    listmax2nd = max(inList2)
    inList2.remove(listmax2nd)
    inList2 += [listmax1st-1] + [listmax2nd-1]
    if listmax1st == 0 or listmax2nd == 0:
        break
    else:
        count += 1


print(count)