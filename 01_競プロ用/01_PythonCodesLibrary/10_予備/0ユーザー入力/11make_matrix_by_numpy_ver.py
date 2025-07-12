import sys
import numpy as np
#----------numpyによる行列の作成-------------------
def make_matrix_by_numpy(y, x):
    # y = 縦, x = 横
    readline = sys.stdin.readline    
    matrix = np.full((y,x), "#", str) #任意の文字で埋めた行列 
    for i in range(y):
        matrix[i] = list(map(str, readline().replace('\n','').replace('\r',''))) #行ごとに好きな文字を行列に代入できる
                                                                            #空欄があるときは .split() をつける
                             #↑この部分を int に変えることで要素が int のリストへ
    return matrix
#=====================================================
readline = sys.stdin.readline
y, x = map(int, readline().replace('\n','').replace('\r','').split())
                                                                #空欄がないときは .split()を消す
aMatrix = make_matrix_by_numpy(y, x)

print(aMatrix)

for rowList in aMatrix:
    print(*rowList, sep="")