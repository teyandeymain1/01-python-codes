import sys
#------------------整数のタプル-----------------------
def make_intTuple():
    readline = sys.stdin.readline
    intTuple = tuple(map(int, readline().split()))
    return intTuple
#=====================================================

inTuple1 = make_intTuple()

dateTuple = ("Fri", "Sat", "Sun", "Mon", "Tue", "Wed", "Thu")

date = inTuple1[0]%7

print(dateTuple[date-1])