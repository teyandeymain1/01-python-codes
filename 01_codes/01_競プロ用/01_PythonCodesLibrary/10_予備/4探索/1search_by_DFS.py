import sys
#----------配列の内包表記による行列の作成-------------------
def make_matrix_without_numpy(y):
    #y:縦(列)  
    readline = sys.stdin.readline
    return list(list(map(str, readline().replace('\n','').replace('\r',''))) for _ in [None]*y)
                                                                        #空欄があるときは .split() をつける
                        #↑この部分を int に変えることで要素が int のリストへ
#----------------------------DFSによる探索---------------------------------
def search_by_DFS(argTuple, inMatrix, sLoc):
    #変数定義
      
    #関数本体
    savePoint = [(False, False), (True, sLoc)] 
    flag = True
    while flag:
        (flag, loc) = savePoint.pop()

        #print("flag", flag, "loc:", loc, "savePoint:", savePoint)

        if not flag and not loc:
            answer = "No" 
        elif not flag and loc:
            answer = "Yes"        
        else: 
            retList = solve_problem(argTuple, inMatrix, loc)
            savePoint.extend(retList) #ここをどうにかしてappendに変えたい。
            
            #print("savePoint", savePoint)
            #print()

    return answer
#----------------------(問題によって変える。今回はAtCoder Typical Contest 001 A - 深さ優先探索 用)------------------
def solve_problem(argTuple, inMatrix, loc):
    #変数定義
    (yMax, xMax) = argTuple[0]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    #----以下変更禁止----   
    retList = []
    #----以上変更禁止----  
    #本体
    for (dy, dx) in directions:
        (y, x) = loc
        (nY, nX) = ((y + dy), (x + dx)) #イミュータブルなint型(loc[0]とloc[1]のこと)にすることで参照元との繋がりを断ち切っている。
        #
        if 0 <= nY <= yMax and 0 <= nX <= xMax and inMatrix[nY][nX] == ".":            
            inMatrix[nY][nX] = "s"
            retList.append((True, (nY, nX)))
        elif 0 <= nY <= yMax and 0 <= nX <= xMax and inMatrix[nY][nX] == "g":
            retList.append((False, inMatrix[nY][nX]))
    #----以下変更禁止----
    #返す用のリストの作成
    return retList
#=========================================main=========================================
def main():
    readline = sys.stdin.readline
    y, x = map(int, readline().replace('\n','').replace('\r','').split())
                                                                #空欄がないときは .split() を消す         
    aMatrix = make_matrix_without_numpy(y)  #行列を取得
    #
    #-------------変数定義(問題によって変える。今回はAtCoder Typical Contest 001 A - 深さ優先探索 用)------------
    sLoc = [[y, x] for y, rowList in enumerate(aMatrix) for x, item in enumerate(rowList) if item == "s"]
    #-----------------------ここまで----------------------------    
    #関数の実行
    argTuple = (((y-1), (x-1)), )
    print(search_by_DFS(argTuple, aMatrix, sLoc[0]))

if __name__ == "__main__": 
    main()