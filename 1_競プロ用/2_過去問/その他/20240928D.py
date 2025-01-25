import sys
#----------配列の内包表記による行列の作成-------------------
def make_matrix_without_numpy(varTuple):
    y = varTuple[0] #縦
    x = varTuple[1] #横    
    readline = sys.stdin.readline
    return list(list(map(int, readline().split()))[:x] for _ in [None]*y)
                                                #↑この部分を消すと二次元配列の横の制限がなくなる。
                         #↑この部分を int に変えることで要素が int のリストへ
                         #intの時は[:-1]を消せ
                         #空欄があるときは .split() を使う
#-------------------隣接行列-------------------
def make_adjacency_matrix(varTuple, inMatrix):
    #変数定義
    y = varTuple[0]
    #隣接行列のための空き二次元行列を作成
    adjMatrix = [[0]*y for _ in [None]*y]
    #隣接行列の作成
    for y, x, wgt in inMatrix: #wtは重み       
        adjMatrix[y-1][x-1] = wgt #頂点 = 重み
    return adjMatrix
#----------------------------DFSによる探索---------------------------------
def search_by_DFS(varTuple, inMatrix, sLoc):
    #変数定義
     
    #関数本体
    savePoint = [(False, False), (True, sLoc)] 
    flag = True
    while flag:
        (flag, loc) = savePoint.pop()

        print("flag", flag, "loc:", loc, "savePoint:", savePoint)

        if not flag and not loc:
            answer = "No" 
        elif not flag and loc:
            answer = loc        
        else: 
            retList = solve_problem(varTuple, inMatrix, loc)
            savePoint.extend(retList) #ここをどうにかしてappendに変えたい。
            
            print("savePoint", savePoint)
            print()

    return answer
#----------------------(問題によって変える。今回はAtCoder Typical Contest 001 A - 深さ優先探索 用)------------------
def solve_problem(varTuple, inMatrix, loc):
    #変数定義

    #----以下変更禁止----   
    retList = []
    #----以上変更禁止----   
    #本体
    for rowList in inMatrix:        
            if rowList[loc] == 0:
                continue
            else:
                if varTuple[]
                retList.append((True, (y, x)))
                varTuple

    #----以下変更禁止----
    #返す用のリストの作成
    return retList
#=====================================================

readline = sys.stdin.readline
varTuple1 = tuple(map(int, readline().split()))
            #↑この部分を list か set に変えることで list か set を作ることができる。
N, M = varTuple1

matrix1 = make_matrix_without_numpy((M, N))

make_adjacency_matrix((M, N), matrix1)
