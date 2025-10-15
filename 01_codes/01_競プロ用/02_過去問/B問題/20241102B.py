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
N, = map(int, readline().replace('\n','').replace('\r','').split())
#引数が一つの時はここに , を入れること                      #空欄があるときは .split() をつける

A = make_matrix_without_numpy(N)

Q, = map(int, readline().replace('\n','').replace('\r','').split())
#引数が一つの時はここに , を入れること                      #空欄があるときは .split() をつける

B = make_matrix_without_numpy(Q)

def keisan(d, q, r):
    n = d//q
    if (q*n+r) < d:
        n += 1
    return (q*n+r)

ansList = list()

for num, (q, r) in enumerate(A, 1):
    for (t, d) in B:
        if t == num:
            if d%q==r:
                ansList.append(r)
            else:
                ansList.append(keisan(d, q, r))
        else:
            continue

print(*ansList, sep="\n")