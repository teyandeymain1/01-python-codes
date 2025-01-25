import sys
#----------配列の内包表記による行列の作成-------------------
def make_matrix_without_numpy(y):
    #y:縦(列)  
    readline = sys.stdin.readline
    return list(list(map(int, readline().replace('\n','').replace('\r','').split())) for _ in [None]*y)
                                                                            #空欄がないときは .split() を消す
                        #↑この部分を str に変えることで要素が str のリストへ
#-------------------隣接行列-------------------
def make_adjacency_matrix(size, inMatrix):
    #隣接行列のための空き二次元行列を作成
    adjMatrix = [[0]*size for _ in [None]*size]
    #隣接行列の作成
    #for y, x, wgt in inMatrix: #wgtは重み
    for (y, x) in inMatrix:        
        adjMatrix[y-1][x-1] = 1 #wgt #頂点 = 重み
        adjMatrix[x-1][y-1] = 1 #wgt #無向グラフなので両方向に辺を張る(有向グラフの時は消す)
    return adjMatrix
#----------------------(問題によって変える。今回はAtCoder232のC問題用)------------------
def solve_problem(numOfVtx, inMatrix1, inMatrix2):
    #----以下変更禁止----
    adjMatrix1 = make_adjacency_matrix(numOfVtx, inMatrix1) #隣接行列1を作成
    adjMatrix2 = make_adjacency_matrix(numOfVtx, inMatrix2) #隣接行列2を作成
    #----以上変更禁止----
    #変数定義
    import itertools
    #本体(AtCoder C参照)
    nPrMatrix = itertools.permutations(range(numOfVtx))
    for PList in nPrMatrix:
        flag = True
        for (y, Py) in enumerate(PList):
            for (x, Px) in enumerate(PList):
                
                #print("PList", PList)
                #print("y", y, "x", x)                
                #print("adjMatrix1[y][x]", adjMatrix1[y][x])
                #print("Py", Py, "Px", Px)
                #print("adjMatrix2[Py][Px]", adjMatrix2[Py][Px])
                
                if adjMatrix1[y][x] != adjMatrix2[Py][Px]:
                    flag = False

                    #print("ダメ")
                    
                    break #for (x, Px)~のループを抜ける
            if not flag:
                break #for (y, Py) in~のループを抜ける
        if flag:
            return "Yes" #for PList in~のループを抜ける
    return "No"
#=====================================================
readline = sys.stdin.readline
N, M  = map(int, readline().replace('\n','').replace('\r','').split())
                                                                #空欄がないときは .split()を消す

aMatrix = make_matrix_without_numpy(M)

bMatrix = make_matrix_without_numpy(M)

print(solve_problem(N, aMatrix , bMatrix))