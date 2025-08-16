import sys
#------------------整数のタプル-----------------------
def make_intTuple():
    readline = sys.stdin.readline
    intTuple = tuple(map(int, readline().split()))
    return intTuple
#=====================================================

inTuple1 = make_intTuple()

answerList = list(range(inTuple1[0]))

answerList = answerList[inTuple1[1]:inTuple1[2]+1] + answerList[:inTuple1[1]] + answerList[inTuple1[2]+1:]

print(answerList)