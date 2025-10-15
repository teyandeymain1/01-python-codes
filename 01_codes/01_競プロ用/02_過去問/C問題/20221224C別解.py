from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline()[:-1]))
    return intList
#------------------------------------------------

def compare_neighbor_in_list(rcrsVal, valList, inputList):

    #-----------以下に操作に必要な変数を書く--------------
    valList = [0,0] #一番目の変数が0のペアの個数を記録、二番目の変数が0を見つけた回数を記録
    #----------------ここまで------------------------
    inputList = inputList + ["?"]

    flag = "down"

    for i in range(len(inputList) - 1):
        if inputList[i] == 0 and inputList[i] == inputList[i+1]:
            flag = "up"
        #--------以下に配列内のある要素とその隣の要素を比較したときを操作するコードを書く。以下はダブってる要素のペア数を数えるコード------------
            valList[-1] += 1
        #----------------ここまで----------------------------------
        else:
            if flag == "up":
                valList[-1] += 1
                valList[-2] = valList[-2] + valList[-1] // 2
                valList[-1] = 0
                flag = "down"

    return valList[-2]

inputList1 = make_intList_func()

valList1 = []

count = compare_neighbor_in_list(0, valList1, inputList1)

print(len(inputList1)-count)