import sys
#------------------整数のタプル-----------------------
def make_int_tuple():
    readline = sys.stdin.readline
    returnData = tuple(map(int, readline().split()))
                  #↑この部分を list か set に変えることで list か set を作ることができる。
    return returnData
#------------------整数のタプル-----------------------
def make_int_list():
    readline = sys.stdin.readline
    returnData = tuple(map(int, readline().split()))
                  #↑この部分を list か set に変えることで list か set を作ることができる。
    return returnData
#=====================================================

inTuple1 = make_int_tuple()

inList1 = make_int_list()
 #↑この部分を list か set に変えることで list か set を作ることができる。

answerList = [1]*inTuple1[0]

for item in inList1:
    if answerList[item-1] == 1:
        answerList[item-1] = 0
    elif answerList[item-1] == 0:
        answerList[item-1] = 1

print(sum(answerList))