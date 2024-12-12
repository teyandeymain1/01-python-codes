import sys
#----------配列の内包表記による行列の作成-------------------
def make_matrix_without_numpy(y):
    #y:縦(列)  
    readline = sys.stdin.readline
    return list(list(map(int, readline().replace('\n','').replace('\r','').split())) for _ in [None]*y)
                                                                        #空欄があるときは .split() をつける
                        #↑この部分を str に変えること
#=====================================================
readline = sys.stdin.readline
H, W = map(int, readline().replace('\n','').replace('\r','').split())
    #引数が一つの時はここに , を入れること                          #空欄がないときは .split() を消す

inMatrix1 = make_matrix_without_numpy(H)

ySumlist = [0]*H
xSumList = [0]*W

rangeOfH = list(range(H))
rangeOfW = list(range(W))
for y in rangeOfH:
    for x in rangeOfW:
        ySumlist[y] += inMatrix1[y][x]
for y in rangeOfH:
    for x in rangeOfW:
        xSumList[x] += inMatrix1[y][x]
for y in rangeOfH:
    for x in rangeOfW:
        inMatrix1[y][x] = ySumlist[y] + xSumList[x] - inMatrix1[y][x]
def print_matrix(inMatrix):
    for rowList in inMatrix:         
        print(" ".join(map(str, rowList)))

print_matrix(inMatrix1)