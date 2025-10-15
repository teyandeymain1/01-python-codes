import sys
#----------------------------DFSによる探索---------------------------------
def search_by_DFS(inDict, start, goal):
    #関数本体
    savePoints = [("failure", -1), ("continue", start)] 
    answer = "No"
    while True:
        (flag, target) = savePoints.pop()

        #print("flag", flag, " target:",  target, "savePoints:", savePoints)

        if flag == "success":
            answer = "Yes"
        elif flag == "continue":
            retList = solver(list(), inDict, target, start, goal)
            savePoints.extend(retList) #ここをどうにかしてappendに変えたい。        
        else: break #flag == "failure"
            
            #print("savePoints", savePoints)
            #print()

    return answer
#----------------------(問題によって変える。今回はAtCoder Typical Contest 001 A - 深さ優先探索 用)------------------
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
                ans = inDict.pop((nY, nX))
                retList.append(("success", ans))
            elif inDict[(nY, nX)] == ".":
                inDict.pop((nY, nX))
                retList.append(("continue", (nY, nX)))
            else: continue    
        else: continue
        #print(inDict)
    #----以下変更禁止----
    return retList
#======================================================================================


#----------配列の内包表記による行列の作成-------------------
def make_matrix(y):
    #y:縦(列)  
    readline = sys.stdin.readline
    return list(list(map(str, readline().replace('\n','').replace('\r',''))) for _ in [None]*y)
                                                                        #空欄があるときは .split() をつける
                        #↑この部分を str に変えることで要素が str のリストへ
#-------------------------座標と要素を見つけて辞書にまとめる----------------------
def find_target_in_matrix(inMatrix, target1, target2, target3):
    #二次元配列から座標と要素を取り出して辞書に保存する。
    return dict(((y, x), item)\
                    for y, rowList in enumerate(inMatrix, start=0)\
                        for x, item in enumerate(rowList, start=0) if item == target1 or item == target2 or item == target3)
#=========================================main=========================================

def main():
    readline = sys.stdin.readline
    y, x = map(int, readline().replace('\n','').replace('\r','').split())
                                                                #空欄がないときは .split() を消す      
    aDict = find_target_in_matrix(make_matrix(y), ".", "s", "g")
    #
    #-------------変数定義(問題によって変える。今回はAtCoder Typical Contest 001 A - 深さ優先探索 用)------------
    for key in aDict:
        if aDict[key] == "s":
            sLoc = key
        elif aDict[key] == "g":
            gLoc = key
        else: continue
    #-----------------------ここまで----------------------------    
    #関数の実行
    print(search_by_DFS(aDict, sLoc, gLoc))

if __name__ == "__main__": 
    main()