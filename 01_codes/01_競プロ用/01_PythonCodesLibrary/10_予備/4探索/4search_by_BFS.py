import sys
#----------配列の内包表記による行列の作成-------------------
def make_matrix_without_numpy(y):
    #y:縦(列)  
    readline = sys.stdin.readline
    return list(list(map(str, readline().replace('\n','').replace('\r',''))) for _ in [None]*y)
                                                                        #空欄があるときは .split() をつける
                        #↑この部分を int に変えることで要素が int のリストへ
#----------------------------BFSによる探索---------------------------------
def search_by_BFS(argTuple, inMatrix, sLoc):
    #変数定義
    
    #関数本体
    from collections import deque       
    savePoint = deque()
    savePoint.append((True, sLoc))    
    flag = True
    while flag:
        (flag, loc) = savePoint.popleft()

        #print("flag", flag, "loc:", loc, "savePoint:", savePoint)

        if not flag and not loc:
            answer = -1 
        elif not flag and loc:
            answer = loc        
        else: 
            retList = solve_problem(argTuple, inMatrix, loc)
            savePoint.extend(retList) #ここをどうにかしてappendに変えたい。
            
            #print("savePoint", savePoint)
            #print(*inMatrix, sep="\n")
            #print()

    return answer
#----------------------(問題によって変える。今回はAtCoder Typical Contest 002 A - 幅優先探索 用)------------------
def solve_problem(argTuple, inMatrix, loc):
    #変数定義
    (yMax, xMax) = argTuple[0]
    (ySt, xSt) = argTuple[1] 
    (yGoal, xGoal) = argTuple[2]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    inMatrix[ySt][xSt] = 0 #スタートとゴール位置の設定
    inMatrix[yGoal][xGoal] = "g"    
    #----以下変更禁止----   
    retList = []
    #----以上変更禁止----      
    #本体
    for (dy, dx) in directions:
        (y, x) = loc
        (nY, nX) = ((y + dy), (x + dx)) #イミュータブルなint型(loc[0]とloc[1]のこと)にすることで参照元との繋がりを断ち切っている。
        #
        if 0 <= nY <= yMax and 0 <= nX <= xMax and inMatrix[nY][nX] == ".":          
            inMatrix[nY][nX] = inMatrix[y][x] + 1
            retList.append((True, (nY, nX)))
        elif 0 <= nY <= yMax and 0 <= nX <= xMax and inMatrix[nY][nX] == "g":
            inMatrix[nY][nX] = inMatrix[y][x] + 1
            retList.append((False, inMatrix[nY][nX]))
    #----以下変更禁止----
    #返す用のリストの作成
    return retList
#======================================main==============================================-
def main():
    readline = sys.stdin.readline
    y, x = map(int, readline().replace('\n','').replace('\r','').split())
                                                                #空欄がないときは .split() を消す         
    #
    #-------------変数定義(問題によって変える。今回はAtCoder Typical Contest 002 A - 幅優先探索 用)------------
    (sy, sx) = tuple(map(int, readline().replace('\n','').replace('\r','').split()))  #スタート位置を取得
    (gy, gx) = tuple(map(int, readline().replace('\n','').replace('\r','').split()))  #ゴール位置を取得     
    aMatrix = make_matrix_without_numpy(y) #行列を取得    
    #-----------------------ここまで----------------------------    
    #関数の実行
    argTuple = (((y-1), (x-1)),  (sy-1, sx-1), ((gy-1), (gx-1)))
    print(search_by_BFS(argTuple, aMatrix, (sy-1, sx-1)))
    
if __name__ == "__main__": 
    main()