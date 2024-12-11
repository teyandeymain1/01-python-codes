from sys import stdin
import numpy as np
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------
#----------numpyによる行列の作成-------------------
def make_matrix_numpy_ver(rcrsVal, valList, inputList):

    row = 2 #縦
    col = 2 #横

    matrix = np.full((row,col), 0, int) #任意の文字で埋めた行列 

    for i in range(row):
        matrix[i] = make_intList_func() #行ごとに好きな文字を行列に代入できる

    return matrix
#---------------------------------------

valList1 = make_intList_func()
inputList = []

matrix1 = make_matrix_numpy_ver(0, valList1, inputList)

print(matrix1[valList1[0]-1][valList1[1]-1])
