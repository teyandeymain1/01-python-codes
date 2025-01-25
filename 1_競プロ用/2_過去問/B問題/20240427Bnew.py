import sys
#------------------整数のタプル-----------------------
def make_int_tuple():
    readline = sys.stdin.readline
    returnData = tuple(map(int, readline().split()))
                  #↑この部分を list か set に変えることで list か set を作ることができる。
    return returnData
#------------------リストの作成-----------------------
def make_list():
    readline = sys.stdin.readline
    returnList = list(map(str, readline()[:-1]))
                          #↑この部分を int に変えることで要素が int のリストへ
                          #intの時は[:-1]を消せ
                          #空欄があるときは .split() を使う
    return returnList
#----------配列の内包表記による行列の作成-------------------
def make_matrix_without_numpy(varList):
    #縦
    y = int(varList[0])
    matrix = [make_list() for _ in [0]*y]
    return matrix
#=====================================================

varList1 = make_int_tuple()

matrix1 = make_matrix_without_numpy(varList1)

matrix2 = make_matrix_without_numpy(varList1)

for y, rowList in enumerate(matrix1):
    if rowList != matrix2[y]:
        for x, item in enumerate(rowList):
            if item != matrix2[y][x]:
                print(y+1, x+1)
                break