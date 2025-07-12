from sys import stdin
import numpy as np
import math
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------
#----------numpyによる行列の作成-------------------
def make_matrix_numpy_ver(rcrsVal, valList, inputList):

    row = valList[0] #縦
    col = 2 #横

    matrix = np.full((row,col), 0, int) #任意の文字で埋めた行列 

    for i in range(row):
        matrix[i] = make_intList_func() #行ごとに好きな文字を行列に代入できる

    return matrix
#---------------------------------------

valList1 = make_intList_func()
inputList = []
valList2 = make_intList_func()

matrix1 = make_matrix_numpy_ver(0, valList1, inputList)

print(matrix1)

row = valList1[0]

resultTmp = 0
result = 0


for i in (valList1[1]-1):
    eucDistance = math.sqrt((matrix1[i-1][0]**2-matrix1[0])+(inputList1[1]-inputListtmp[1]))
    if resultTmp <= eucDistance:
        result = eucDistance
        resultTmp = eucDistance

print(result)
