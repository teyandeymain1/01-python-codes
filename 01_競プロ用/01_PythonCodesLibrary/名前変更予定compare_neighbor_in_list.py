import sys
#------------------整数のリスト-----------------------
def make_intList():
    readline = sys.stdin.readline
    intList = list(map(int, readline()[:-1]))
    return intList
#------------------------------------------------
#-------------------配列内の連続して並んでいる要素の個数を数える----------------------
def compare_neighbor_in_list(rcrsVar, varList, inputList):

    #-----------以下に操作に必要な変数を書く--------------
    varList = [0,0] #一番目の変数が0のペアの個数を記録、二番目と三番目の変数が0を見つけた回数を記録
    #----------------ここまで------------------------
    inputList = inputList + ["?"]

    print(inputList)
    print(inputList[:-1])

    flag = "down"
    contNumTmp = 0

    for index, item in (enumerate(inputList[:-1])):
        if 0 == 0 and inputList[index] == inputList[index+1]:
            flag = "up"
        #--------以下に配列内のある要素とその隣の要素を比較したときを操作するコードを書く。以下はダブってる要素のペア数を数えるコード------------
            varList[-1] += 1 #0を見つけた回数を記録
            contNumTmp += 1  #0を見つけた回数を記録
        #----------------ここまで----------------------------------
        else:
            if flag == "up":
                varList[-1] += 1 #0を見つけた回数を記録
                contNumTmp += 1

                print("連続個数Tmp: " + str(contNumTmp) )

                varList[-2] += contNumTmp // contNumTmp
                contNumTmp = 0
                flag = "down"

        #フラグの変化に注目。
        #初めて隣接する二つの項が同じだと判明したとき、回数を記録することができていない。
        #だから、フラグがupからdownに切り替わる瞬間に回数を一つ追加する。
        print(str(index) + ": " + flag + " / ダブり数:" + str(varList[-1]) + " / ペア数:" + str(varList[-2]))

    return varList
#--------------------------------------------------------------------
inputList1 = make_intList()

varList1 = [0]

#---------関数内に追加したい変数を配列の最後に追加------------- 
#----------------------ここまで-----------------------------

answerList = compare_neighbor_in_list(0, varList1, inputList1)

print("連続してダブっている要素の数: " +str(answerList[-1]))
print("連続する要素を一組にした時のペア数(AtCoderのABC283のC-Cash Register参照): " +str(answerList[-2]))