from sys import stdin
import numpy as np
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------

inputList1 = make_intList_func()

row = int(3**inputList1[0]) #縦
col = int(3**inputList1[0]) #横

matrix1 = np.full((row,col), "#", str)

for i in range(row):
    print(*matrix1[i], sep="")
