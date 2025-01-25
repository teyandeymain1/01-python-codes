from sys import stdin
import numpy as np
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
#----------numpyによる行列の作成-------------------
def make_matrix_numpy_ver_func(rcrsVar, varList, inputList):

    row = int(varList) #縦
    col = int(varList) #横

    matrix = np.full((row,col), "X", str) #任意の文字で埋めた行列 

    for i in range(row):
        matrix[i] = make_strList_func() #行ごとに好きな文字を行列に代入できる

    return matrix
#---------------------------------------

varList1 = make_intList_func()

answer = "No"

if varList1[0] == 0 or varList1[1] == 0:
    answer = "No"

elif varList1[0] == varList1[1]:
    matrix1 = make_matrix_numpy_ver_func(0, varList1[0], 0)
    matrix2 = make_matrix_numpy_ver_func(0, varList1[1], 0)
    if (matrix1 == matrix2).all() == True:
        answer = "Yes"

elif varList1[0] > varList1[1]:
    matrix1 = make_matrix_numpy_ver_func(0, varList1[0], 0)
    matrix2 = make_matrix_numpy_ver_func(0, varList1[1], 0)

    for i in range(varList1[0]-varList1[1]+1):
        for j in range(varList1[0]-varList1[1]+1):

            print("縦: " + str(i) +", "+ str(i+varList1[1]) + " 横: " + str(j) +", "+ str(j+varList1[1]))
            print(matrix1[i:i+varList1[1], j:j+varList1[1]])
            
            if (matrix1[i:i+varList1[1], j:j+varList1[1]] == matrix2).all() == True:
                answer = "Yes"

print(answer)