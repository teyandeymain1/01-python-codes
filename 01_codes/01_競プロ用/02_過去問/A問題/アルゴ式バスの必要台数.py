import sys
#------------------整数のタプル-----------------------
def make_intTuple():
    readline = sys.stdin.readline
    intTuple = tuple(map(int, readline().split()))
    return intTuple
#=====================================================

inTuple1 = make_intTuple()

answer = inTuple1[0]//inTuple1[1]

if inTuple1[0]%inTuple1[1] == 0:
    print(answer)
else:
    print(answer+1)