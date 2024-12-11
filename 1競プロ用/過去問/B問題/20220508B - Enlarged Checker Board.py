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


list1 = make_intList_func()

rowNum = int(list1[0]) #行数
rowSet = int(list1[1]) #行のセット数
col = int(list1[2]) #横


cookieCoordinate = np.zeros((rowNum*rowSet, col*rowNum),dtype=str)

print(*cookieCoordinate)

