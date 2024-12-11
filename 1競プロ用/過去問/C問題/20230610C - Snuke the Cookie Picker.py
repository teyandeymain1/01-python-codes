import numpy as np

#----------------------------------------------
def make_intList_func():
    intList = list(map(int, input().split()))
    return intList
#------------------------------------------------
#-----------------文字のリスト-----------------------
def make_strList_func():
    strList = list(map(str, input()))
    return strList
#------------------------------------------------
#-------------全探索-------------------
def seach_exhaustive_func(val1, val2, list):

    rowStart = 1000000000000000000000000000000
    colStart = 1000000000000000000000000000000
    rowEnd = 0
    colEnd = 0
    i = 0
    j = 0
    answerRow = 0
    answerCol = 0

    for i in range(val1):
        for j in range(val2):
            #---------以下に関数内で行う操作を書く---------
            if list[i][j] == "#":
                if i < rowStart:
                    rowStart = i
                if j < colStart:
                    colStart = j
                if rowEnd < i:
                    rowEnd = i
                if colEnd < j:
                    colEnd = j   
            #--------------ここまで------------------
    for k in range(rowStart, rowEnd + 1):
        for l in range(colStart, colEnd + 1):
            if list[k][l] == ".":
                answerRow = k
                answerCol = l
    print((answerRow + 1), (answerCol + 1))
#---------------------------------------

list1 = make_intList_func()

row = int(list1[0]) #縦
col = int(list1[1]) #横

cookieCoordinate = np.zeros((row, col),dtype=str)

for i in range(row):
    cookieCoordinate[i] = make_strList_func()

seach_exhaustive_func(row, col, cookieCoordinate)
