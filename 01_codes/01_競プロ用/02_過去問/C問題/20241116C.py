import sys
import itertools
#------------------整数の行-----------------------
readline = sys.stdin.readline
N, K = map(int, readline().replace('\n','').replace('\r','').split())

#------------------整数のタプル-----------------------
readline = sys.stdin.readline
sList = list(map(int, readline().replace('\n','').replace('\r','')))

sList.append(9)

bufList = []
groupList = []
for i in range(len(sList)-1):
    if sList[i] == sList[i+1]:
        bufList.append(sList[i])
    else:
        bufList.append(sList[i])
        groupList.append(bufList)
        bufList = []
   
counter =  0
for i, item in enumerate(groupList):
    if item[0] == 1:
        counter += 1
        if counter == K:
            buf = groupList[i]
            groupList[i] = groupList[i-1]
            groupList[i-1] = buf
    else:
        continue

ansList = list(itertools.chain.from_iterable(groupList))

print(*ansList, sep="")