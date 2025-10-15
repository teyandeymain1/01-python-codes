import sys
#----------配列の内包表記による行列の作成-------------------
def make_matrix_without_numpy(y):
    #y:縦(列)  
    readline = sys.stdin.readline
    return list(list(map(int, readline().replace('\n','').replace('\r','').split())) for _ in [None]*y)
                                                                        #空欄があるときは .split() をつける
                        #↑この部分を str に変えることで要素が str のリストへ
#=====================================================
readline = sys.stdin.readline
N, M = map(int, readline().replace('\n','').replace('\r','').split())
#引数が一つの時はここに , を入れること                      #空欄があるときは .split() をつける

aMatrix = make_matrix_without_numpy(M)

reservedSet = set()

for (y, x) in aMatrix:
    reservedSet.add((y, x))

    if y+2 <= N and x+1 <= N:
        reservedSet.add((y+2, x+1))
    if y+1 <= N and x+2 <= N:
        reservedSet.add((y+1, x+2))
    if y-1 >= 1 and x+2 <= N:
        reservedSet.add((y-1, x+2))
    if y-2 >= 1 and x+1 <= N:
        reservedSet.add((y-2, x+1))
    if y-2 >= 1 and x-1 >= 1:
        reservedSet.add((y-2, x-1)) 
    if y-1 >= 1 and x-2 >= 1:
        reservedSet.add((y-1, x-2))
    if y+1 <= N and x-2 >= 1:
        reservedSet.add((y+1, x-2))
    if y+2 <= N and x-1 >= 1:
        reservedSet.add((y+2, x-1))

ans = N**2 - len(reservedSet)

print(ans)