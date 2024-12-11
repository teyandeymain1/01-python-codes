from sys import stdin
import sys
#------------------整数のリスト-----------------------
def make_intList():
    readline = stdin.readline
    intList = list(map(int, readline()[:-1].split()))
    return intList
#---------------昇順でリストをソート---------------
def sort_list_asc(list):
    list = sorted(list, reverse=False) #昇順
    return list
#-------------------二分探索-----------------------
def search_binary(varList, inputList):
    N, M = varList[0], varList[1]
    left, right = 0, max(inputList) #探索する範囲の左端と右端を設定
    while left <= right:                 
        mid = (left + right) // 2 #探索する範囲の中央を計算   
        total = sum(min(mid, item) for item in inputList)
        if total <= M:
            left = mid + 1 #中央の値より大きい場合は探索範囲の左を変える
        else:
            right = mid - 1 #中央の値より小さい場合は探索範囲の右を変える
        print("mid", mid, "left:", left, "right:", right, "total:", total)
    return right            # 見つからなかった場合
#==============================================================
varList1 = make_intList()
N = varList1[0]
M = varList1[1]

inputList1 = make_intList()

answer = 0
if sum(inputList1) <= M:
    print("infinite")
    sys.exit()
else:
    answer = search_binary(varList1, inputList1)

print(answer)