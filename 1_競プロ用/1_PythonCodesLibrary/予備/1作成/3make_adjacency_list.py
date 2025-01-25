import sys
#----------配列の内包表記による行列の作成-------------------
def make_matrix_without_numpy(y):
    #y:縦(列)  
    readline = sys.stdin.readline
    return list(list(map(int, readline().replace('\n','').replace('\r','').split())) for _ in [None]*y)
                                                                            #空欄がないときは .split() を消す
                        #↑この部分を str に変えることで要素が str のリストへ
#-------------------隣接リスト-------------------
def make_adjacency_list(numOfVtx, inMatrix):
    #隣接行列のための空き二次元行列を作成
    adjDict = dict((vtx, dict()) for vtx in range(numOfVtx))
    #隣接行列1の作成
    #for y, x, wgt in inMatrix: #wtは重み
    for (y, x) in inMatrix:   
        adjDict[y-1][x-1] = 1 #wgt #頂点 = 重み
        adjDict[x-1][y-1] = 1 #wgt #無向グラフなので両方向に辺を張る(有向グラフの時は消す)
    return adjDict
#----------------------(問題によって変える。今回はAtCoder232のC問題用)------------------
def solve_problem(numOfVtx, inMatrix1, inMatrix2):
    #----以下変更禁止----
    adjDict1 = make_adjacency_list(numOfVtx, inMatrix1) #隣接リスト1作成
    adjDict2 = make_adjacency_list(numOfVtx, inMatrix2) #隣接リスト2作成
    #----以上変更禁止----
    #変数定義
    import itertools
    #本体(AtCoder C参照)
    rangeTuple = tuple(range(numOfVtx))
    nPrMatrix = itertools.permutations(rangeTuple)
    for PList in nPrMatrix:
        flag = True
        for vtx1 in rangeTuple:
            vtxSet1 = set(adjDict1[PList[vtx1]])
            vtxSet2 = set(PList[vtx2] for vtx2 in adjDict2[vtx1]) #このコードの意味は？
            
            #print(adjDict1)
            #print(adjDict2)
            #print("PList", PList)
            #print("vtx1:", vtx1, "vtxList1:", vtxSet1, "vtxList2:", vtxSet2)

            if vtxSet1 != vtxSet2: #高橋君のボールiの隣接リストと青木君のボールperm[i-1]の隣接リストを比較
                flag = False

                #print("ダメ")

                break #for vtx1 in~のループを抜ける
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