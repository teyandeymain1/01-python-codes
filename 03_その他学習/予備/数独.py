import time
import sys
import copy
sys.setrecursionlimit(10**6) #再帰回数の変更
#--------------------------------------整数のリスト----------------------------------------
def make_intList():
    readline = sys.stdin.readline
    intList = list(map(int, readline()[:-1]))
    return intList
#-------------------------配列の内包表記による行列の作成-------------------------------------
def make_matrix_without_numpy(varList):
    matrix = [make_intList() for _ in [None]*varList[0]]
    return matrix
#============================数独を解くプログラム============================================
#-------------------------空欄の座標を取得し、内包表記を用いて配列に記録----------------------
def find_empty(inputMatrix):
    #配列の中にタプルを代入
    emptyLocList = [(r, c) for r, rowList in enumerate(inputMatrix) for c, item in enumerate(rowList) if item == 0] #"for r, rowList"->"for c, item"の順で動く 
    #for r, rowList in enumerate(inputMatrix) #行
        #for c, item in enumerate(rowList)    #列
            #if item == 0
                #emptyLocList.append((int(r), int(c))) #座標(r,c)のアイテムが0ならemptyLocListにタプルで追加
    if len(emptyLocList) == 0:
        return -1 #空欄が無い(0が無い)とき、-1を返す。
    else:
        return emptyLocList
#------------------------使用済みの数字を記録する集合(行)の作成------------------------------
def make_rowSet(varList, inputMatrix):
    #1行を丸々取得する
    rowSet = set(inputMatrix[varList]) 
    return rowSet
#-----------------------使用済みの数字を記録する集合(列)の作成-------------------------------
def make_colSet(varList, inputMatrix):
    #二次元配列を"for rowList"1つで回すと、一行ごとに取得できる。
    colSet = {rowList[varList] for rowList  in inputMatrix} 
    return colSet
#----------------------使用済みの数字を記録する集合(3×3マス内)の作成-------------------------
def make_SqSet(varList, inputMatrix):
    #変数定義
    row, col = (varList[0]//3)*3, (varList[1]//3)*3
    threeSqList = []
    #
    for i in range(3):
        threeSqList.extend(inputMatrix[row+i][col:(col+3)]) #[row+i]は行、[col:(col+3)]は列範囲。つまり3列を3行取得してthreeSqListに加える
    threeSqSet = set(threeSqList)
    return threeSqSet
#-----------------------------答え候補の集合を作成-----------------------------------
def make_answerSet(varList, varSet, inputMatrix):
    #変数定義
    row, col = varList[0], varList[1]
    #集合作成
    existSet = make_rowSet(row, inputMatrix).union(make_colSet(col, inputMatrix), make_SqSet(varList, inputMatrix)) #行、列、3×3の集合を合体
    answerSet = varSet - existSet #引数として与えられた1~9までの数を要素とする集合からexistSetを引く。    
    return answerSet
#------------------(座標)=key, (答え候補の集合)=valueとして辞書を作成-------------------
def make_answerDicts(varSet, inputMatrix):
    #変数定義
    emptyLocList = find_empty(inputMatrix) 
    #辞書作成
    if emptyLocList == -1: #find_emptyが-1を返す(空欄が無い)とき、-1を返す。
        return -1, -1
    else:
        answerDict = {loc: make_answerSet(loc, varSet, inputMatrix) for loc in emptyLocList}   #辞書を作成
        sortedValues = sorted(answerDict.items(), key=lambda item:len(item[1]), reverse=False) #valuesをソート--False 昇順 True 降順--    
        answerDict = {keyTmp: valueTmp for keyTmp, valueTmp in sortedValues}                   #ソートしたvaluesで辞書を再作成
        #print("answerDict:", answerDict)
        keyList = list(answerDict)     #ソートした辞書からkeyをリストとして取得
        loc = keyList[0]               #"keyList"の先頭、つまり昇順にソートした辞書の先頭の要素(keyなので座標)を取り出す。
        ansSetInDict = answerDict[loc] #"keyList"から取得した座標の答え候補集合を取得
        return loc, ansSetInDict
#-----------------------候補の少ないマスから数字を代入する-----------------------------
def search_answer(varList, inputMatrix):
    #変数定義
    intSet = varList[-3]        #各マスに入るすべての数字の候補(9×9の数独なら1~9まで)
    savedMatrixList = varList[-2]
    savePoint = varList[-1]
    loc, ansSetInDict = make_answerDicts(intSet, inputMatrix) #make_answerDictsが-1を返す(find_emptyが-1を返す)とき、-1を返す。
    
    if loc == -1: #与えられた数独に空欄がないとき
        return -1
    elif len(ansSetInDict) == 1: #答え候補が1個なら代入
        inputMatrix[loc[0]][loc[1]] = ansSetInDict.pop() #答え候補集合から答えを取得し代入 
        #print("座標: (", loc[0]+1, ",", loc[1]+1, ") 答え:", inputMatrix[loc[0]][loc[1]], "残り:", ansSetInDict)
        return 0 #"0"は継続
    elif len(ansSetInDict) > 1: #答え候補が2個以上で深さ探索を起動
        #print("深さ探索起動")
        savedMatrixList.append(copy.deepcopy(inputMatrix)) #値を代入するまえに数独を"savedMatrixList"に保管
        inputMatrix[loc[0]][loc[1]] = ansSetInDict.pop()   #とりあえず答え候補の一つを取得し代入
        #print("座標: (", loc[0]+1, ",", loc[1]+1, ") 仮の答え:", inputMatrix[loc[0]][loc[1]], "残り:", ansSetInDict)
        savePoint.append([copy.deepcopy(loc), copy.deepcopy(ansSetInDict)]) #とりあえず代入したときの[座標, 答え候補集合の残り]を"savaPoint"に保管
        #print("savePoint", savePoint)
        return 0
    elif len(ansSetInDict) < 1: #答え候補がないとき、深さ探索を再起動
        #print("深さ探索再起動")
        inputMatrix = savedMatrixList.pop() #最も直近で分岐したときの数独の盤面に戻す&"savedMatrixList"からその盤面を削除
        #print("savePoint前", savePoint)
        savePointTmp = savePoint.pop() #最も直近で分岐したときの[座標, 答え候補集合の残り]をリセットした盤面に代入する&"savePoint"から代入した情報を削除
        #print("savePoint後", savePoint)
        loc, ansSetInDict = savePointTmp[0], savePointTmp[1]
        inputMatrix[loc[0]][loc[1]] = ansSetInDict.pop()
        #print("座標: (", loc[0]+1, ",", loc[1]+1, ") 答え:", inputMatrix[loc[0]][loc[1]], "残り:", ansSetInDict)
        return inputMatrix
#----------------------------------数独を解く:メイン---------------------------------------
def solve_Sudoku_main(varList, inputMatrix):
    #変数定義
    size = int(varList[0]) #サイズ
    #関数を動かす条件  
    if size%3 != 0:
        sys.exit("数独のサイズを3の倍数で入力して下さい。")
    else:
        flag = search_answer(varList, inputMatrix)
    #再帰関数の実行
    if flag == -1:
        print_matrix(inputMatrix) #flagが"-1"(空欄が一つもない)とき、数独を表示する関数を実行。
        #解いた数独の正誤評価関数の実行    
        print(is_Sudoku_correct(varList, inputMatrix)) 
    elif flag == 0: #flagが"0"(継続)とき、"solve_Sudoku_main"を再帰。 
        #print_matrix(inputMatrix)
        solve_Sudoku_main(varList, inputMatrix)
    else:
        #print("盤面リセット")
        #print_matrix(flag)
        solve_Sudoku_main(varList, flag)
#----------------------------------数独を表示する---------------------------------------
def print_matrix(inputMatrix):
    print("---答え---")
    for row1 in inputMatrix:         
        print(*row1, sep="")
#---------------------------解いた数独が正しいか確認する---------------------------------
def is_Sudoku_correct(varList, inputMatrix):
    #変数定義
    intSet = varList[-3] #各マスに入るすべての数字の候補(9×9の数独なら1~9まで)
    #
    for r, rowList in enumerate(inputMatrix):
        for c, item in enumerate(rowList):
            varList = (r, c)
            judgeSet = make_answerSet(varList, intSet, inputMatrix)
            if len(judgeSet) > 0:
                return "正しい答えでありません。"
            else:
                continue
    return "正しい答えです。"
#=========================================main=========================================
def main():
    print("数独のサイズを入力してください。(数字は3の倍数にしてください。)")
    varList1 = make_intList() #数独のサイズを入力する。
    print("数独を入力してください。ただし、空欄は0で埋めてください。")
    matrix1 = make_matrix_without_numpy(varList1)
    #-----時間測定開始------
    start = time.time()
    #変数定義
    savedMatrixList = []
    savePoint = []
    varList1.extend([set(range(1, varList1[0]+1)), savedMatrixList, savePoint]) #各マスに入るすべての数字の候補(9×9の数独なら1~9まで)
    #関数の実行
    solve_Sudoku_main(varList1, matrix1)
    #----------時間測定終了-----------
    end = time.time()
    print("実行時間:", (end - start))

if __name__ == "__main__": 
    main()