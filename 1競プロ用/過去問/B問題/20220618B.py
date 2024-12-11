from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------

valList1 = make_intList_func()

intList1 = make_intList_func()

pieceList = []

for i in range(valList1[0]):
    pieceList.append(0)
    for j in range(len(pieceList)):
        pieceList[j] = pieceList[j] + intList1[i]

count = 0
for j in range(len(pieceList)):
    if pieceList[j]>=4:
        count += 1

print(count)
