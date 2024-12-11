import time
import sys
sys.setrecursionlimit(10**6) #再帰回数の変更
from sys import stdin
#--------------------------------------整数のリスト----------------------------------------
def make_intList():
    readline = stdin.readline
    intList = list(map(int, readline()[:-1]))
    return intList
#-------------------------配列の内包表記による行列の作成-------------------------------------
def make_matrix_without_numpy(varList):

    matrix = [make_intList() for _ in [None]*varList[0]]

    return matrix
#============================数独を解くプログラム============================================
#-------------------------空欄の座標を取得し、内包表記を用いて配列に記録----------------------
def find_empty(inputMatrix):

    emptyLocList = [(r, c) for r, rowList in enumerate(inputMatrix) for c, item in enumerate(rowList) if item == 0] #"for r, rowList"->"for c, item"の順で動く 
    #for r, rowList in enumerate(inputMatrix) #行
        #for c, item in enumerate(rowList)    #列
            #if item == 0
                #emptyLocList.append((int(r), int(c))) #座標(r,c)のアイテムが0ならemptyLocListにタプルで追加

    if len(emptyLocList) == 0: #空欄が無い(0が無い)とき、-1を返す。
        return -1
    else:
        return emptyLocList
#------------------------使用済みの数字を記録する集合(行)の作成------------------------------
def make_rowSet(varList, inputMatrix):
    
    rowSet = set(inputMatrix[varList]) #1行を丸々取得する

    return rowSet
#-----------------------使用済みの数字を記録する集合(列)の作成-------------------------------
def make_colSet(varList, inputMatrix):

    colSet = {rowList[varList] for rowList  in inputMatrix} #二次元配列を"for rowList"1つで回すと、一行ごとに取得できる。

    return colSet
#----------------------使用済みの数字を記録する集合(3×3マス内)の作成-------------------------
def make_SqSet(varList, inputMatrix):

    #変数定義
    row = (varList[0]//3)*3
    col = (varList[1]//3)*3
    threeSqList = []

    for i in range(3):
        threeSqList.extend(inputMatrix[row+i][col:(col+3)]) #[row+i]は行、[col:(col+3)]は列範囲。つまり3列を3行取得してthreeSqListに加える
    threeSqSet = set(threeSqList)

    return threeSqSet
#-----------------------------答え候補の集合を作成-----------------------------------
def make_answerSet(varList, varSet, inputMatrix):

    #変数定義
    row = varList[0]
    col = varList[1]
    #集合作成
    existSet = make_rowSet(row, inputMatrix).union(make_colSet(col, inputMatrix), make_SqSet(varList, inputMatrix)) #行、列、3×3の集合を合体
    answerSet = varSet - existSet #引数として与えられた1~9までの数を要素とする集合からexistSetを引く。

    #print("使用済み:", "row", row+1, "col", col+1, existSet)    

    return answerSet
#------------------(座標)=key, (答え候補の集合)=valueとした辞書を作成-------------------
def make_answerDicts(varSet, inputMatrix):

    #変数定義
    emptyLocList = find_empty(inputMatrix) 
    #辞書作成
    if emptyLocList == -1: #find_emptyが-1を返す(空欄が無い)とき、-1を返す。
        return -1
    else:
        answerDict = {loc: make_answerSet(loc, varSet, inputMatrix) for loc in emptyLocList} #辞書を作成
        sortedValues = sorted(answerDict.items(), key=lambda item:len(item[1]), reverse=False)         #valuesをソート--False 昇順 True 降順--
        answerDict = {keyTmp: valueTmp for keyTmp, valueTmp in sortedValues}                 #ソートしたvaluesで辞書を再作成

        print("answerDict:", answerDict)

        return answerDict
#-----------------------候補の少ないマスから数字を代入する-----------------------------
def search_answer(varSet, inputMatrix):

    answerDict= make_answerDicts(varSet, inputMatrix)

    if answerDict == -1: #make_answerDictsが-1を返す(find_emptyが-1を返す)とき、-1を返す。
        return -1, -1
    else: #変数定義
        keyList = list(answerDict)
        loc = keyList[0]
        ansDictValSet = answerDict[loc]
        answerTmp = next(iter(ansDictValSet))
        inputMatrix[loc[0]][loc[1]] = answerTmp

        print("座標: (", loc[0]+1, loc[1]+1, ") 答え候補:", ansDictValSet, "仮答え", answerTmp)

        #数字を代入する
        if len(ansDictValSet) > 1: #もし答えの候補が複数ある場合、座標&別の仮の答え(代入したものを除いた残りの集合の先頭の要素)を返す。
            ansDictValSet.discard(answerTmp)
            return loc, next(iter(ansDictValSet)) 
        else:
            return -10, -10 #"-10 -10"は答えの候補が一つしかないときのフラグ
#----------------------------------数独を解く:メイン---------------------------------------
def solve_Sudoku_main(varList, inputMatrix):

    #変数定義
    size = int(varList[0]) #サイズ
    intSet = varList[1]    #各マスに入るすべての数字の候補(9×9の数独なら1~9まで)

    #関数を動かす条件  
    if size%3 != 0:
        sys.exit("数独のサイズを3の倍数で入力して下さい。")

    #変数定義
    loc, answerTmp = search_answer(intSet, inputMatrix)

    #print("判定:", answerTmp)

    #関数の実行
    if answerTmp == -10:  #search_answerが"-10 -10"を返す(あるマスに入る答えの候補が一つしかなかった)とき、次のマスの探索を実行。
        
        print_matrix(inputMatrix)
        
        solve_Sudoku_main(varList, inputMatrix)
    elif answerTmp == -1: #search_answerが"-1 -1"を返す(空欄が一つもない)とき、inputMatrixを表示する関数を実行。
        print_matrix(inputMatrix)
    else:
        print_matrix(inputMatrix)

        solve_Sudoku_main(varList, inputMatrix)
#----------------------------------数独を表示する---------------------------------------
def print_matrix(inputMatrix):
    for row2 in inputMatrix:
        print(row2)
    for row1 in inputMatrix:   
        print(*row1, sep="")
#=========================================main=========================================
def main():

    print("数独のサイズを入力してください。(数字は3の倍数にしてください。)")
    readline = stdin.readline
    varList1 = list(map(int, readline().split())) #数独のサイズを入力する。

    print("数独を入力してください。ただし、空欄は0で埋めてください。")
    matrix1 = make_matrix_without_numpy(varList1)

    #-----時間測定開始------
    start = time.time()
    #変数定義
    varList1.append(set(range(1, varList1[0]+1))) #各マスに入るすべての数字の候補(9×9の数独なら1~9まで)
    #関数の実行
    solve_Sudoku_main(varList1, matrix1)
    #----------時間測定終了-----------
    end = time.time()
    print("実行時間:", (end - start))

if __name__ == "__main__": 
    main()