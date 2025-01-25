import sys
import math
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

aMatrix = make_matrix_without_numpy(N)

ans = 0
for i in range(1, (M+1), 1):
    ans += i

for (l, r) in aMatrix:
    buf = 0
    if l < r:
        for p in range(l, (r+1), 1):
            buf += (M-p)
    elif l > r:
        for q in range(r, (l+1), 1):
            buf += (M-q)
    else: # l = r
        ans -= 1

    print(buf)

    ans = ans - buf               

print(ans)