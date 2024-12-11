import sys
sys.setrecursionlimit(10**6) #再帰回数の変更
#------------------------------------------------
def search_linearly_recursive_ver_func(rcrsVar, varList, inputList):  #変数は順に("ループ回数","変数リスト","操作するリスト")  

    #停止条件
    if rcrsVar == 0:
        return -1
    
    #------------------再帰関数内で行う操作を下記に書く(このプログラムはAtCoder ABC081B_Shift only用)-------------------
    varList[0] = inputList1[(varList[0] - 1)]
    varList[1] += 1

    if varList[0] == 2:
        return varList[1]

    #----------------------ここまで-----------------------------

    #関数を関数内で呼び出す
    return search_linearly_recursive_ver_func((rcrsVar - 1), varList, inputList)
#------------------------------------------------

varNum = int(input())

inputList1 = []

for i in range(varNum):
    inputList1 += [int(input())]

varList1 = [1, 0]

print(search_linearly_recursive_ver_func((10**5-1), varList1, inputList1))