from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------
#-----------------文字のリスト-----------------------
def make_strList_func():
    readline = stdin.readline
    strList = list(map(str, readline()[:-1]))
    return strList
#------------------------------------------------
#----------配列の内包表記による行列の作成-------------------
def make_matrix_without_numpy_ver_func(rcrsVar, varList, inputList):

    matrix = [([100000] + make_strList_func() + [100000]) for _ in [0]*varList[0]] 

    addList = [100000]*(varList[1]+2)

    matrix.append(addList)

    matrix.insert(0, addList) 

    return matrix
#---------------------------------------------------------

varList1 = make_intList_func()

rcrsVar = 0
inputList1 = []

matrix1 = make_matrix_without_numpy_ver_func(rcrsVar, varList1, inputList1)

matrix2 = [([100000] + [0]*varList1[1] + [100000]) for _ in [0]*varList1[0]] 
addList = [100000]*(varList1[1]+2)
matrix2.append(addList)
matrix2.insert(0, addList) 

for i, item1 in enumerate(matrix1):
    for j, item2 in enumerate(matrix1):
        if matrix1[i][j] == "#":
            matrix2[i-1][j-1] += 1
            matrix2[i-1][j] += 1
            matrix2[i-1][j+1] += 1

            matrix2[i][j-1] += 1
            matrix2[i][j+1] += 1

            matrix2[i+1][j-1] += 1
            matrix2[i+1][j] += 1
            matrix2[i+1][j+1] += 1

for i, item1 in enumerate(matrix1):
    for j, item2 in enumerate(matrix1):
        if matrix1[i][j] == ".":
            matrix1[i][j] = matrix2[i][j]

for k in range(1, (varList1[0]+1)):
    print(*matrix1[k][1:(varList1[1]+1)], sep="")