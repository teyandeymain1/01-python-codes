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

    matrix = [(make_strList_func()) for _ in [0]*varList[0]] 

    return matrix
#---------------------------------------------------------

inputList1 = make_intList_func()

inputList2 = make_intList_func()

matrix1 = make_matrix_without_numpy_ver_func(0, inputList1, 0)

inputList4 = make_strList_func()

notEmptyListRow = []
notEmptyListColumn = []

for i, row in enumerate(matrix1):
    for j, item in enumerate(row):
        if item == "#":
            notEmptyListRow += [i+1]
            notEmptyListColumn += [j+1]

print(notEmptyListRow)
print(notEmptyListColumn)

for k in inputList4:
    if k == "U" and inputList2[0] > 1:
        inputList2[0] -= 1
        if (inputList2[0], inputList2[1]) in zip(notEmptyListRow, notEmptyListColumn):
            inputList2[0] += 1

    elif k == "D" and inputList2[0] < inputList1[0]:
        inputList2[0] += 1
        if (inputList2[0], inputList2[1]) in zip(notEmptyListRow, notEmptyListColumn):
            inputList2[0] -= 1

    elif k == "L" and inputList2[1] > 1:
        inputList2[1] -= 1
        if (inputList2[0], inputList2[1]) in zip(notEmptyListRow, notEmptyListColumn):
            inputList2[1] += 1

    elif k == "R" and inputList2[1] < inputList1[1]:
        inputList2[1] += 1
        if (inputList2[0], inputList2[1]) in zip(notEmptyListRow, notEmptyListColumn):
            inputList2[1] -= 1

    print(*inputList2)



print("----")

print(*inputList2)