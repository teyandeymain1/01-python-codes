import sys
#----------配列の内包表記による行列の作成-------------------
def make_matrix_without_numpy(y):
    #y:縦(列)  
    readline = sys.stdin.readline
    return list(list(map(int, readline().replace('\n','').replace('\r',''))) for _ in [None]*y)
                                                                        #空欄があるときは .split() をつける
                        #↑この部分を str に変えることで要素が str のリストへ
#=====================================================
readline = sys.stdin.readline
y, = map(int, readline().replace('\n','').replace('\r',''))
#引数が一つの時はここに , を入れること                      #空欄があるときは .split() をつける

aMatrix = make_matrix_without_numpy(y)

print(aMatrix)

aMatrix[0][0] = "?"
aMatrix[1][1] = "?"

print(aMatrix)