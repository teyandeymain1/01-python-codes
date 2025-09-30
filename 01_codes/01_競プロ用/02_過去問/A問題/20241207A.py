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
y, = map(int, readline().replace('\n','').replace('\r','').split())
#引数が一つの時はここに , を入れること                      #空欄がないときは .split() を消す

aMatrix = make_matrix_without_numpy(y)

left = aMatrix[0][1]
for i in range(1, y, 1):
    addition = aMatrix[i][1]
    time = aMatrix[i][0] - aMatrix[i-1][0]


    if left - time < 0:
        left = addition
    else:
        left -= time
        left += addition

print(left)
