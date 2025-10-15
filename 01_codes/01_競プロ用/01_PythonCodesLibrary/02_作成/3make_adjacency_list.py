import sys
#----------配列の内包表記による行列の作成-------------------
def mk_mtrx(y):
    #y:縦(列)  
    readline = sys.stdin.readline
    return list(list(map(int, readline().replace('\n','').replace('\r','').split())) for _ in [None]*y)
                                                                            #空欄がないときは .split() を消す
#-------------------隣接リスト-------------------
def mk_adj_list(vtxs, matrix):
    #隣接リストのための空き二次元リストを作成
    adjDict = dict((vtx, dict()) for vtx in range(vtxs))
    #隣接リストの作成
    #for (y, x), wgt in matrix: #wtは重み
    for (y, x) in matrix:   
        adjDict[y-1][x-1] = 1 #wgt #頂点 = 重み
        adjDict[x-1][y-1] = 1 #wgt #無向グラフなので両方向に辺を張る(有向グラフの時はコメントアウト)
    return adjDict
#----------------------(問題によって変える。今回はAtCoder232のC問題用)------------------
def solver(vtxs, matrix1, matrix2):
    #変数定義
    import itertools
    adjDict1 = mk_adj_list(vtxs, matrix1) #隣接リスト1作成
    adjDict2 = mk_adj_list(vtxs, matrix2) #隣接リスト2作成
    #本体(AtCoder C参照)
    rangeTuple = tuple(range(vtxs))
    nPrList = itertools.permutations(rangeTuple)
    for ps in nPrList:
        flag = True
        for vtx1 in rangeTuple:
            vtxSet1 = set(adjDict1[ps[vtx1]])
            vtxSet2 = set(ps[vtx2] for vtx2 in adjDict2[vtx1]) #このコードの意味は？
            
            #print(adjDict1)
            #print(adjDict2)
            #print("ps", ps)
            #print("vtx1:", vtx1, "vtxList1:", vtxSet1, "vtxList2:", vtxSet2)

            if vtxSet1 != vtxSet2: #高橋君のボールiの隣接リストと青木君のボールperm[i-1]の隣接リストを比較
                flag = False

                #print("ダメ")

                break #for vtx1 in~のループを抜ける
        if flag:
            return "Yes" #for ps in~のループを抜ける
    return "No"
#======================================main==============================================-
def main():
    readline = sys.stdin.readline
    N, M  = map(int, readline().replace('\n','').replace('\r','').split())
                                                                #空欄がないときは .split()を消す
    xMx = mk_mtrx(M)
    yMx = mk_mtrx(M)
    print(solver(N, xMx , yMx))

if __name__ == "__main__": 
    main()