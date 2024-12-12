import sys
#------------------整数のタプル-----------------------
def make_int_tuple_list_set():
    readline = sys.stdin.readline
    return tuple(map(int, readline().split()))
            #↑この部分を list か set に変えることで list か set を作ることができる。
#------------------リストの作成-----------------------
def make_list():
    readline = sys.stdin.readline
    return list(map(int, readline().split()))
                    #↑この部分を int に変えることで要素が int のリストへ
                    #intの時は[:-1]を消せ
                    #空欄があるときは .split() を使う
#----------配列の内包表記による行列の作成-------------------
def make_matrix_without_numpy(varList):
    #縦
    y = int(varList[0])
    return [make_list() for _ in [0]*y]
#=====================================================

inTuple1 = make_int_tuple_list_set()
 #↑この部分を list か set に変えることで list か set を作ることができる。

matrix1 = make_matrix_without_numpy(inTuple1)

answer = matrix1[0][0]
for j in range(1, inTuple1[0]):

    i = answer-1

    #print(i+1, j+1)

    if i < j:
        answer = matrix1[j][i]
    elif i >= j:
        answer = matrix1[i][j]                    

print(answer)
