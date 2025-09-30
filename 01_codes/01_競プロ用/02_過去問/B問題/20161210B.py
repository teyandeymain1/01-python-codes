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
def make_matrix_numpy_ver(rcrsVal, valList, inputList):

    row = int(valList[0]) #縦
    col = int(valList[1]) #横

    matrix = np.full((row,col), " ", str) #任意の文字で埋めた行列 

    for i in range(-1, row):
        if i == -1:
            continue
        else:
            matrix[i] = make_strList_func() #行ごとに好きな文字を行列に代入できる

    return matrix
#---------------------------------------

valList1 = make_intList_func()

inputList = []
matrix1 = make_matrix_numpy_ver(0, valList1, inputList)

row = valList1[0]
for i in range(row):
    for j in range(2):
        print(*matrix1[i], sep="")