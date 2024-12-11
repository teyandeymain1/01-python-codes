import sys
#------------------整数のタプル-----------------------
def make_intTuple():
    readline = sys.stdin.readline
    intTuple = tuple(map(int, readline().split()))
    return intTuple

varTuple = make_intTuple()

num = 0

while True:
    if varTuple[0] < varTuple[1]:
        print(varTuple[0])
        sys.exit()
    elif (varTuple[0] - varTuple[1]*num) < 0:
        break
    else:
        answer = varTuple[0] - (varTuple[1]*num)
        num += 1

print(answer)