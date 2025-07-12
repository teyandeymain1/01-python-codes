from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#-------------------------------------------------------
#-----------------文字のリスト-----------------------
def make_strList_func():
    readline = stdin.readline
    strList = list(map(str, readline()[:-1]))
    return strList
#------------------------------------------------
#----------配列の内包表記による行列の作成-------------------
def make_matrix_without_numpy_ver_func(rcrsVar, varList, inputList):

    matrix = [make_strList_func() for _ in range(varList)]

    return matrix
#---------------------------------------------------------

varList1 = make_intList_func()

matrixMid = make_matrix_without_numpy_ver_func(0, varList1[0], 0)

matrixUp = [("#") for _ in range(varList1[1]+2)]
print(*matrixUp, sep="")

for i in range(varList1[0]):

    matrixMid[i].insert(0, "#")
    matrixMid[i] += ["#"]
    print(*matrixMid[i], sep="")

matrixLow = [("#") for _ in range(varList1[1]+2)]
print(*matrixLow, sep="")