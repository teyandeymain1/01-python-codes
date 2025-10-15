import sys
#----------配列の内包表記による行列の作成-------------------
def make_matrix_without_numpy(varTuple):
    readline = sys.stdin.readline
    y = int(varTuple[0]) #縦
    return list(list(map(int, readline().split())) for _ in [0]*y)
                         #↑この部分を int に変えることで要素が int のリストへ
                         #intの時は[:-1]を消せ
                         #空欄があるときは .split() を使う
#-------------------隣接行列-------------------
def make_adjacency_matrix(varTuple, inMatrix, wgtDict):
    #変数定義
    y = varTuple[0]
    wgt = 1 #重み
    #隣接行列のための空き二次元行列を作成
    adjMatrix = [[0]*y for _ in [None]*y]
    #隣接行列の作成
    for (y, x) in inMatrix:
        adjMatrix[y-1][x-1] = wgt #頂点 = 重み
        adjMatrix[x-1][y-1] = wgt #無向グラフなので両方向に辺を張る(有向グラフの時は消す)
    return adjMatrix
#----------------------(問題によって変える。今回はAtCoder232のC問題用)------------------
def solve_problem(varTuple, inMatrix1, inMatrix2, wgtDict):
    #----以下変更禁止----
    adjMatrix1 = make_adjacency_matrix(varTuple, inMatrix1, wgtDict) #隣接行列1を作成
    adjMatrix2 = make_adjacency_matrix(varTuple, inMatrix2, wgtDict) #隣接行列2を作成
    #----以上変更禁止----

    #変数定義
    import itertools
    numOfvtx = varTuple[0] #頂点数
    #本体(AtCoder C参照)
    nPrMatrix = itertools.permutations(range(numOfvtx))
    MinCost = 10*7
    for PList in nPrMatrix:
        BufCost = 0
        for (y, Py) in enumerate(PList):
            for (x, Px) in enumerate(PList):
                
                #print("PList", PList)
                #print("y", y, "x", x)                
                #print("adjMatrix1[y][x]", adjMatrix1[y][x])
                #print("Py", Py, "Px", Px)
                #print("adjMatrix2[Py][Px]", adjMatrix2[Py][Px])
                
                if adjMatrix1[y][x] != adjMatrix2[Py][Px]:

                    print("PList", PList)
                    print("y", y, "x", x)                
                    print("adjMatrix1[y][x]", adjMatrix1[y][x])
                    print("Py", Py, "Px", Px)
                    print("adjMatrix2[Py][Px]", adjMatrix2[Py][Px])                    
                    print("BufCost", wgtDict[(Py, Px)])

                    BufCost += wgtDict[(Py, Px)]

                    print("ダメ")

        if BufCost < MinCost:
            MinCost = BufCost
    return MinCost
#=====================================================

N = int(input())
Mg = int(input())

matrix1 = make_matrix_without_numpy((Mg, N))

Mh = int(input())

matrix2 = make_matrix_without_numpy((Mh, N))

#-------------------------座標と要素を見つけて辞書にまとめる----------------------
def find_loc_in_matrix(inMatrix):
    #二次元配列から座標と要素を取り出して辞書に保存する。
    return {(y, x): item\
                for y, rowList in enumerate(inMatrix, start=0)\
                    for x, item in enumerate(rowList, start=(y+1))}
#---------------------------------------------
matrix3 = make_matrix_without_numpy((Mh, (N-1)))
wgtDict = find_loc_in_matrix(matrix3)

print(solve_problem((N,), matrix1, matrix2, wgtDict))

