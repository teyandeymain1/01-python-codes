import sys
from itertools import *
#------------------整数のタプル-----------------------
def make_intTuple():
    readline = sys.stdin.readline
    intTuple = tuple(map(int, readline().split()))
    return intTuple
#---------------------------------- 行列を表示する---------------------------------------
def print_matrix(inputMatrix):
    print("---答え---")
    for row1 in inputMatrix:         
        print(" ".join(map(str,row1)))
#-----------------配列内の要素の組み合わせを全列挙-------------------------
def make_combi(varList, inputList):
    #変数定義
    #-----------以下に操作に必要な変数を書く--------------
    N = varList[0]
    K = varList[1]
    numList = [tuple(range(1, (i + 1))) for i in inputList]
    #--------------------ここまで-----------------------
    #
    print(*numList)
    print(list(product(*numList)))
    returnList = list(x for x in list(product(*numList)) if sum(x)%K == 0) #<-二つ目の変数が組合せの数を作る
    return returnList
#=========================================main=========================================
def main():
    varTuple1 = make_intTuple()
    N = varTuple1[0]
    K = varTuple1[1]
    inputTuple1 = make_intTuple()

    answerMatrix = make_combi(varTuple1, inputTuple1)

    print_matrix(answerMatrix)
    
if __name__ == "__main__": 
    main()