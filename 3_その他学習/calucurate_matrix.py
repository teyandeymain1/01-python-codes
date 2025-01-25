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

print("計算")
print("1.行列の積 2.逆行列 3.行列式 4.固有値")
select = int(input())

y1, x1 = map(int, readline().replace('\n','').replace('\r','').split())
                                                                #空欄がないときは .split()を消す
xMx = mk_np_mtrx(y1, x1)

if select == 1:
    y2, x2 = map(int, readline().replace('\n','').replace('\r','').split())
                                                                #空欄がないときは .split()を消す
    yMx = mk_np_mtrx(y2, x2)
    print("行列の積")
    print(xMx@yMx)
elif select == 2:
    print("逆行列")
    print()
elif select == 3:
    print("行列式")
    print()
elif:
    print("固有値")
    print()
else:
    print("Error")
