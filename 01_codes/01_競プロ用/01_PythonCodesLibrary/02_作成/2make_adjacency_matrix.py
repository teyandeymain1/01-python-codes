import sys
#----------(int)内包表記による行列作成(int)-------------------
def mk_mtrx(y):
    #y:縦(列)  
    readline = sys.stdin.readline
    return list(list(map(int, readline().replace('\n','').replace('\r','').split())) for _ in [None]*y)
                                                                        #空欄があるときは .split() をつける
#-------------------隣接行列-------------------
def mk_adj_mtrx(size, matrix):
    #隣接行列のための空き二次元行列を作成
    adjMatrix = [[0]*size for _ in [None]*size]
    #隣接行列の作成
    #for (y, x), wgt in matrix: #wgtは重み
    for (y, x) in matrix:        
        adjMatrix[y-1][x-1] = 1 #wgt #頂点 = 重み
        adjMatrix[x-1][y-1] = 1 #wgt #無向グラフなので両方向に辺を張る(有向グラフの時はコメントアウト)
    return adjMatrix
#----------------------(問題によって変える。今回はAtCoder232のC問題用)------------------
def solver(vtxs, matrix1, matrix2):
    #変数定義
    import itertools
    adjMatrix1 = mk_adj_mtrx(vtxs, matrix1) #隣接行列1を作成
    adjMatrix2 = mk_adj_mtrx(vtxs, matrix2) #隣接行列2を作成
    #本体(AtCoder C参照)
    nPrList = itertools.permutations(range(vtxs))
    for ps in nPrList:
        flag = True
        for (y, py) in enumerate(ps):
            for (x, px) in enumerate(ps):
                
                #print("ps", ps)
                #print("y", y, "x", x)                
                #print("adjMatrix1[y][x]", adjMatrix1[y][x])
                #print("py", py, "px", px)
                #print("adjMatrix2[py][px]", adjMatrix2[py][px])
                
                if adjMatrix1[y][x] != adjMatrix2[py][px]:
                    flag = False

                    #print("ダメ")
                    
                    break #for (x, px)~のループを抜ける
            if not flag:
                break #for (y, py) in~のループを抜ける
        if flag:
            return "Yes" #for ps in~のループを抜ける
    return "No"
#======================================main==============================================-
def main():
    readline = sys.stdin.readline
    n, m = map(int, readline().replace('\n','').replace('\r','').split())
                                                                    #空欄がないときは .split()を消す

    xMx = mk_mtrx(m)
    yMx = mk_mtrx(m)
    print(solver(n, xMx , yMx))

if __name__ == "__main__":
    main()