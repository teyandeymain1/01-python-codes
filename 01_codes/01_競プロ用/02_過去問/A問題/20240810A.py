import sys
#------------------整数のリスト-----------------------
def make_intList():
    readline = sys.stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#-----------------文字のリスト-----------------------
def make_strList():
    readline = sys.stdin.readline
    strList = list(map(str, readline()[:-1].split()))
    return strList
#=====================================================

inputList1 = make_intList()

N, T, A = inputList1[0], inputList1[1], inputList1[2]

nokori = N - (T+A)

minTohyo = min(T, A)
maxTohyo = max(T, A)

if (nokori+minTohyo) > maxTohyo:
    print("No")
else:
    print("Yes")