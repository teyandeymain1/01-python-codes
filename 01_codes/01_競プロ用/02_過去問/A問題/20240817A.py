import sys
#------------------整数のリスト-----------------------
def make_intList():
    readline = sys.stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#=====================================================

inputList1 = make_intList()

A, B, C = inputList1[0], inputList1[1], inputList1[2]

if A <= 12:
     A += 24
if B <= C:
    B += 24
if C < A < B:
        print("Yes")
else:
    print("No") 