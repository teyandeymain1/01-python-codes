import sys
#------------------整数のタプル-----------------------
def make_intTuple():
    readline = sys.stdin.readline
    intTuple = tuple(map(int, readline().split()))
    return intTuple
#------------------整数のタプル-----------------------
def make_intList():
    readline = sys.stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#=====================================================

inTuple1 = make_intTuple()

intList1 = make_intList()

answerList = intList1[-inTuple1[1]:] + intList1[:-inTuple1[1]]


print(*answerList)