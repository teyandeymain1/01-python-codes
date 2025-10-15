import sys
#------------------整数のタプル-----------------------
def make_intTuple():
    readline = sys.stdin.readline
    intTuple = tuple(map(int, readline().split()))
    return intTuple
#=====================================================

inTuple1 = make_intTuple()

count = 0
for i in range(1, inTuple1[0]+1):
    if i%3 == 0:
        count += 1

print(count)