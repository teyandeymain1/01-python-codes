import numpy as np

#------------------整数のリスト-----------------------
def make_intList_func():
    intList = list(map(int, input().split()))
    return intList
#-----------------------------------------------

inputList1 = make_intList_func()

row = int(inputList1[1]) #縦
col = 2 #横

cookieCoordinate = np.zeros((row, col),dtype=int)

for i in range(row):
    cookieCoordinate[i] = make_intList_func()


for j in range(row):
    for k in range(2):
        if cookieCoordinate[j][k] == cookieCoordinate[j+1][k]:
            
