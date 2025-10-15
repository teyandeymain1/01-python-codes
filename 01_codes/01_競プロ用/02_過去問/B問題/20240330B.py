import sys
from itertools import chain,combinations
#------------------整数のタプル-----------------------
def make_int_tuple():
    readline = sys.stdin.readline
    returnData = tuple(map(str, readline()[:-1]))
                  #↑この部分を list か set に変えることで list か set を作ることができる。
    return returnData
#=====================================================

inTuple1 = make_int_tuple()
 #↑この部分を list か set に変えることで list か set を作ることができる。

bufList1 = []
for i in range(len(inTuple1)+1):
    bufList1 += list(combinations(inTuple1, i)) #<-二つ目の変数が組合せの数を作る

answerList = []
for item in bufList1:
    bufStr = "".join(item)
    print(bufStr)
    answerList += bufStr
    print(answerList)

print(set(answerList))
print(len(set(answerList)))


eum