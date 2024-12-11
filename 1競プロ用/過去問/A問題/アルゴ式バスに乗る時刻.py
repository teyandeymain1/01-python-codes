import sys
#------------------整数のタプル-----------------------
def make_intTuple():
    readline = sys.stdin.readline
    intTuple = tuple(map(int, readline().split()))
    return intTuple
#=====================================================

inTuple1 = make_intTuple()

answer = inTuple1[1]//inTuple1[0]

if inTuple1[1]%inTuple1[0] == 0:
    print(inTuple1[0]*answer)
else:
    print(inTuple1[0]*(answer+1))
