import sys
#----------------------------BFSによる探索---------------------------------
def search_by_BFS(inDict, start, goal):
    #関数本体
    from collections import deque       
    savePoints = deque()     
    savePoints.append(("continue", start))
    answer = -1
    flag = "continue"    
    while flag == "continue":
        (flag, target) = savePoints.popleft()

        #print("flag", flag, " target:",  target, "savePoints:", savePoints)

        if flag == "success":
            answer = target
        elif flag == "continue":
            retList = solver(list(), inDict, target, start, goal)
            savePoints.extend(retList) #ここをどうにかしてappendに変えたい。        
        else: break
            
            #print("savePoints", savePoints)
            #print(*inMatrix, sep="\n")
            #print()
    return answer
#----------------------(問題によって変える。今回はAtCoder Typical Contest 002 A - 幅優先探索 用)------------------
def solver(retList, inDict, target, start, goal):
    #変数定義
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    inDict[start] = 0 
    #本体
    for (dy, dx) in directions:
        (y, x) =  target
        (nY, nX) = ((y + dy), (x + dx)) #イミュータブルなint型( target[0] と target[1] )にして参照元との繋がりを切る。
        #
        if (nY, nX) in inDict:
            if (nY, nX) == goal:
                inDict[(nY, nX)] = inDict[(y, x)] + 1
                retList.append(("success", inDict[(nY, nX)]))
            elif inDict[(nY, nX)] == ".":
                inDict[(nY, nX)] = inDict[(y, x)] + 1
                retList.append(("continue", (nY, nX)))
            else: continue    
        else: continue
        #print(inDict)
    #----以下変更禁止----
    return retList
#=========================================================================================


#----------配列の内包表記による行列の作成-------------------
def make_matrix(y):
    #y:縦(列)  
    readline = sys.stdin.readline
    return list(list(map(str, readline().replace('\n','').replace('\r',''))) for _ in [None]*y)
                                                                        #空欄があるときは .split() をつける
                        #↑この部分を str に変えることで要素が str のリストへ
#-------------------------座標と要素を見つけて辞書にまとめる----------------------
def find_target_in_matrix(inMatrix, target1):
    #二次元配列から座標と要素を取り出して辞書に保存する。
    return dict(((y, x), item)\
                    for y, rowList in enumerate(inMatrix, start=0)\
                        for x, item in enumerate(rowList, start=0) if item == target1)
#=========================================main=========================================
def main():
    readline = sys.stdin.readline
    y, x = map(int, readline().replace('\n','').replace('\r','').split())
                                                                #空欄がないときは .split() を消す         
    #
    #-------------変数定義(問題によって変える。今回はAtCoder Typical Contest 002 A - 幅優先探索 用)------------
    (sy, sx) = map(int, readline().replace('\n','').replace('\r','').split())  #スタート位置を取得
    (gy, gx) = map(int, readline().replace('\n','').replace('\r','').split())  #ゴール位置を取得     
    aDict = find_target_in_matrix(make_matrix(y), ".")   
    #-----------------------ここまで----------------------------    
    #関数の実行
    print(search_by_BFS(aDict, (sy-1, sx-1), (gy-1, gx-1)))
    
if __name__ == "__main__": 
    main()