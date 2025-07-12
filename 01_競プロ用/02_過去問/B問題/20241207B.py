import sys
import itertools

#----------配列の内包表記による行列の作成-------------------
def make_matrix_without_numpy(y):
    #y:縦(列)  
    readline = sys.stdin.readline
    return list(list(map(str, readline().replace('\n','').replace('\r',''))) for _ in [None]*y)
                                                                        #空欄があるときは .split() をつける
                        #↑この部分を str に変えることで要素が str のリストへ
#=====================================================
readline = sys.stdin.readline
H, W, D = map(int, readline().replace('\n','').replace('\r','').split())

aMatrix = make_matrix_without_numpy(H)

locList = []
for i in range(H):
    for j in range(W):
        if aMatrix[i][j] == ".":
            locList.append((i, j))

pairList = tuple(itertools.combinations(locList, 2))

count = 0
for (x1, y1), (x2, y2) in pairList:

    buf = set()
    for (x, y) in locList:
        if (abs(x1-x) + abs(y1-y)) <= D:
            buf.add((x, y))
        else:
            continue
    for (x, y) in locList:
        if (abs(x2-x) + abs(y2-y)) <= D:
            buf.add((x, y))
        else:
            continue

    if count < len(buf):
        count = len(buf)

    else:
        continue

print(count)