import sys
#----------配列の内包表記による行列の作成-------------------
def make_matrix_without_numpy(y):
    #y:縦(列)  
    readline = sys.stdin.readline
    return list(list(map(str, readline().replace('\n','').replace('\r',''))) for _ in [None]*y)
                                                                        #空欄があるときは .split() をつける
                        #↑この部分を str に変えることで要素が str のリストへ
#=====================================================

sMatrix = make_matrix_without_numpy(8)

reseveYSet = set()
reseveXSet = set()

numSet = set(range(8))

rangeTuple = tuple(range(8))
for y in rangeTuple:
    for x in rangeTuple:
        if sMatrix[y][x] == "#":
            reseveYSet.add(y)
            reseveXSet.add(x)

emptyYSet = numSet - reseveYSet
emptyXSet = numSet - reseveXSet

ans = len(emptyYSet)*len(emptyXSet)

print(ans)