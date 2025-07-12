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
    returnList = list(map(int, readline().split()))
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
import sys
#------------------距離を求める-----------------------
def make_distance(varlist):
    y1 = varlist[0]
    y2 = varlist[1]
    x1 = varlist[2]
    x2 = varlist[3]
    dist = ((y1 - y2)**2) + ((x1 - x2)**2)
    return dist
#=====================================================
varTuple1 = make_int_tuple()
matrix1 = make_matrix_without_numpy(varTuple1)

answerList = [0]*varTuple1[0]

rangeList = list(range(varTuple1[0]))
answerList1 = [make_distance((matrix1[i1][0], matrix1[i2][0], matrix1[i1][1], matrix1[i2][1]))\
                for i1 in rangeList\
                    for i2 in rangeList]
print(answerList1)

for i1 in rangeList:
    maxDist = 0
    for i2 in rangeList:
        dist = make_distance((matrix1[i1][0], matrix1[i2][0], matrix1[i1][1], matrix1[i2][1]))
        if maxDist < dist:
            maxDist = dist
            answerList[i1] = i2 + 1

print(*answerList, sep="\n")