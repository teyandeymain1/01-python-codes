import sys
import copy
#------------------整数のリスト-----------------------
def make_intList():
    readline = sys.stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#-----------------文字のリスト-----------------------
def make_strList():
    readline = sys.stdin.readline
    strList = list(map(str, readline()[:-1]))
    return strList
#----------配列の内包表記による行列の作成-------------------
def make_matrix_without_numpy(varList):
    row = int(varList[0]) #縦
    matrix = [make_strList() for _ in [0]*row]
    return matrix
#----------------------------DFSによる探索---------------------------------
def search_by_DFS(varList, inputMatrix):
    #変数定義
    (yMax, xMax) = ((varList[0] - 1), (varList[1] - 1))
    locOfS = varList[-1]     
    used = [[False] * varList[1] for _ in range(varList[0])]
    print_matrix(used)
    used[locOfS[0]][locOfS[1]] = True
    savePoint = [(-1, -1), copy.deepcopy(locOfS)]  
    answer = "No"
    #関数本体
    while True:
    #for i in [0]*5:
        loc = savePoint.pop()
        print("loc:", loc, "savePoint:", savePoint)
        if loc == (-1, -1):
            break
        else: 
            listForFunc = [loc, (yMax, xMax)]
            returnList, used = solve_problem(listForFunc, inputMatrix, used)
            savePoint.extend(returnList)
            print(savePoint)
    return answer
#----------------------(問題によって変える。今回はAtCoder Typical Contest 001 A - 深さ優先探索 用)------------------
def solve_problem(varList, inputMatrix, used):
    #変数定義
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    locMax = varList[1]
    returnList = []
    #本体
    for (dy, dx) in directions:
        loc = copy.deepcopy(varList[0])
        loc[0] += dy
        loc[1] += dx
        if 0 <= loc[0] <= locMax[0] and 0 <= loc[1] <= locMax[1]:
            if inputMatrix[loc[0]][loc[1]] == "#" or used[loc[0]][loc[1]]: #壁or探索済
                continue
            if inputMatrix[loc[0]][loc[1]] == "g": #ゴール到達
                print("Yes")
                exit()
            used[loc[0]][loc[1]] = True
            returnList.append(loc)     
    #----以下変更禁止----
    #返す用のリストの作成
    print(returnList)
    return returnList, used
#---------------------------------- 行列を表示する---------------------------------------
def print_matrix(inputMatrix):
    print("---答え---")
    for row1 in inputMatrix:         
        print(*row1, sep="")
#=========================================main=========================================
def main():
    varList1 = make_intList()                     #サイズを取得
    matrix1 = make_matrix_without_numpy(varList1) #行列を取得
    #
    #-------------変数定義(問題によって変える。今回はAtCoder Typical Contest 001 A - 深さ優先探索 用)------------
    locOfS = [[y, x] for y, rowList in enumerate(matrix1) for x, item in enumerate(rowList) if item == "s"]
    varList1.extend(locOfS)
    #-----------------------ここまで----------------------------    
    #関数の実行
    print(search_by_DFS(varList1, matrix1))

if __name__ == "__main__": 
    main()

