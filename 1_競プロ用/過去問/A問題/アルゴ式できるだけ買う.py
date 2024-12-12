import sys
#------------------整数のタプル-----------------------
def make_intTuple():
    readline = sys.stdin.readline
    intTuple = tuple(map(int, readline().split()))
    return intTuple
#=====================================================

inTuple1 = make_intTuple()

otsuri = inTuple1[0]
ryoukin = inTuple1[1]
i = 0

while True:
    if  otsuri- ryoukin*i < 0:
        break
    else:
        i += 1

print(i-1)