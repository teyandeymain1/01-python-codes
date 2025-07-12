import sys
import collections
#------------------整数のタプル-----------------------
def make_int_data_struct():
    readline = sys.stdin.readline
    return tuple(map(int, readline().split()))
            #↑この部分を list か set に変えることで list か set を作ることができる。
#------------------リストの作成-----------------------
def make_list():
    readline = sys.stdin.readline
    return list(map(str, readline().split()))
                    #↑この部分を int に変えることで要素が int のリストへ
                    #intの時は[:-1]を消せ
                    #空欄があるときは .split() を使う
#----------配列の内包表記による行列の作成-------------------
def make_matrix_without_numpy(varList):
    #縦
    y = int(varList[1])
    return [make_list() for _ in [0]*y]
#=====================================================
varTuple1 = make_int_data_struct()
matrix1 = make_matrix_without_numpy(varTuple1)

dictA = dict()

houseList = []
answerList = []

for rowList in matrix1:
    if rowList[1] == "M" and rowList[0] not in houseList:
        houseList.append(rowList[0])
        answerList.append("Yes")
    else:
        answerList.append("No")

print(*answerList, sep = "\n")