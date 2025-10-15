import sys
#------------------整数のタプル-----------------------
def make_int_tuple_list_set():
    readline = sys.stdin.readline
    returnData = tuple(map(int, readline().split()))
            #↑この部分を list か set に変えることで list か set を作ることができる。
    return returnData
#=====================================================

inTuple1 = make_int_tuple_list_set()
 #↑この部分を list か set に変えることで list か set を作ることができる。

answerList = list(range(inTuple1[0]*2))
emptyList = []

for i in range(inTuple1[0]):
    emptyList += [answerList.pop(0)] + [answerList.pop(-1)]

print(emptyList)