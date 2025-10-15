import sys
#----------配列の内包表記による行列の作成-------------------
def make_matrix_without_numpy(y):
    #y:縦(列)  
    readline = sys.stdin.readline
    return list(list(map(int, readline().replace('\n','').replace('\r','').split())) for _ in [None]*y)
                                                                            #空欄がないときは .split() を消す
                           #↑この部分を str に変えることで要素が str のリストへ
#------------------距離を求める-----------------------
def make_distance(loc1, loc2):
    (x1, y1) = loc1
    (x2, y2) = loc2
    return (((x1 - x2)**2) + ((y1 - y2)**2))
#----------------------(問題によって変える。今回は座標をx, yの形で取得して各点の距離を返す)------------------
def solve_answer(inMatrix):
    limit = len(inMatrix)
    return dict(((tuple(inMatrix[i]), tuple(inMatrix[j])), make_distance(inMatrix[i], inMatrix[j]))\
                        for i in range(limit) for j in range(limit))
    #return list(make_distance(inMatrix[i], inMatrix[j]) for i in range(limit) for j in range(limit))
#=====================================================
readline = sys.stdin.readline
y, = map(int, readline().replace('\n','').replace('\r','').split())
#引数が一つの時はここに , を入れること                          #空欄がないときは .split()を消す
aMatrix = make_matrix_without_numpy(y)
#

print(solve_answer(aMatrix))