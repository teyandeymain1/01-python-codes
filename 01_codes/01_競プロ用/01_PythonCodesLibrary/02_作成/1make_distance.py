import sys
#----------(int)内包表記による行列作成(int)-------------------
def mk_mtrx(y):
    #y:縦(列)  
    readline = sys.stdin.readline
    return list(list(map(int, readline().replace('\n','').replace('\r','').split())) for _ in [None]*y)
                                                                        #空欄があるときは .split() をつける
#------------------距離を求める-----------------------
def mk_dist(loc1, loc2):
    (x1, y1) = loc1
    (x2, y2) = loc2
    return ((x1 - x2)**2) + ((y1 - y2)**2)
#----------------------(問題によって変える。今回は座標をx, yの形で取得して各点の距離を返す)------------------
def solver(matrix):
    xys = len(matrix)
    return dict(((tuple(matrix[x]), tuple(matrix[y])), mk_dist(matrix[x], matrix[y]))\
                        for x in range(xys) for y in range(xys))
    #return list(mk_dist(matrix[x], matrix[y]) for i in range(xys) for j in range(xys))
#=====================================================

readline = sys.stdin.readline
y1, = map(int, readline().replace('\n','').replace('\r','').split())
#引数が一つの時はここに , を入れること                          #空欄がないときは .split()を消す
xMx = mk_mtrx(y1)
#

print(solver(xMx))
