import sys
import numpy as np
#----------(str)numpyによる行列の作成(str)-------------------
def mk_np_mtrx(y, x):
    # y = 縦, x = 横
    readline = sys.stdin.readline    
    matrix = np.full((y, x), "#", str) #任意の文字で埋めた行列 
    for i in range(y):
        matrix[i] = list(map(str, readline().replace('\n','').replace('\r',''))) #行ごとに好きな文字を行列に代入できる
                                                                            #空欄があるときは .split() をつける
    return matrix
#=====================================================


import sys
import numpy as np
#----------(int)numpyによる行列の作成(int)-------------------
def mk_np_mtrx(y, x):
    # y:縦(列), x:横(行)
    readline = sys.stdin.readline    
    matrix = np.full((y, x), 0, int) #任意の文字で埋めた行列 
    for i in range(y):
        matrix[i] = list(map(int, readline().replace('\n','').replace('\r','').split())) #行ごとに好きな文字を行列に代入できる
                                                                            #空欄があるときは .split() をつける
    return matrix
#=====================================================

readline = sys.stdin.readline
y1, x1 = map(int, readline().replace('\n','').replace('\r','').split())
                                                                #空欄がないときは .split()を消す
xMx = mk_np_mtrx(y1, x1)

print(xMx)

for rowList in xMx:
    print(*rowList, sep="")
