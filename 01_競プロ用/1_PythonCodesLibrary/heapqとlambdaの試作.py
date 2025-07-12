import sys
from heapq import *

tupleList = [(1, 2), (4, 7), (0, 4), (7, 8), (3, 3)]
heapify(tupleList)
print(tupleList)
print("最小値", heappop(tupleList))

tupleList = list(map(lambda tupleA: (tupleA[0]*(-1), tupleA[1]), tupleList))

heapify(tupleList)
print(tupleList)
tupleListMax = heappop(tupleList)
tupleListMax = (tupleListMax[0]*(-1), tupleListMax[1])
print("最大値", tupleListMax)