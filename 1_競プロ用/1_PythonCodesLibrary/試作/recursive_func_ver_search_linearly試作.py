import sys
sys.setrecursionlimit(10**6) #再帰回数の変更
#------------------整数のリスト-----------------------
def make_intList():
    readline = sys.stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------
#------------------------------------------------
def search_linearly_recursive_ver(rcrsVar, varList, inputList):  #変数は順に("ループ回数","変数リスト","操作するリスト")  

    #停止条件
    if rcrsVar == 0:
        return varList[0]
    
    #------------------再帰関数内で行う操作を下記に書く(このプログラムはAtCoder ABC081B_Shift only用)-------------------
    result = 0         #答えの候補を保存するための変数
    swich = 0          #探索を止めるための変数
    while swich == 0:  #swich = 0の間は探索を続行

        if (inputList[rcrsVar - 1] % 2) == 0:  #探索を続ける条件
            inputList[rcrsVar - 1] = inputList[rcrsVar - 1] // 2
            result += 1
        else:
            swich = 1 #swich = 1 として探索を止める

    print(varList)
    print("-A1: " + str(varList[-1])) 
    print("--B1: " + str(result))

    if result < varList[-1]: #--答えの候補を保存する条件を左に書く--
        varList[0] = result
        varList[-1] = result #配列の最後に記録した最小値を更新する。

    print("---A2: " + str(varList[-1]))
    print("----B2: " + str(varList[0]))
    #----------------------ここまで-----------------------------

    #関数を関数内で呼び出す
    return search_linearly_recursive_ver((rcrsVar - 1), varList, inputList)
#------------------------------------------------

varList1 = make_intList() #変数リストを作成

#---------再帰関数内に追加したい変数を配列の最後に追加-----
varList1 = varList1 + [1000000000000000000000000000000000000000000000000000000000000] #最小値を配列の最後に追加 
#----------------------ここまで-----------------------------

inputList1 = make_intList()

#---------関数内に追加したい変数を配列の最後に追加------------- 
#----------------------ここまで-----------------------------

print(search_linearly_recursive_ver(int(varList1[0]), varList1, inputList1)) #変数リストの最初の要素がループ回数