from sys import stdin
from itertools import *
import math
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline()[:-1].split()))
    return intList
#------------------------------------------------
#-----------------文字のリスト-----------------------
def make_strList_func():
    readline = stdin.readline
    strList = list(map(str, readline()[:-1]))
    return strList
#------------------------------------------------
#-----------------配列内の要素の組み合わせを全列挙-------------------------
def make_combi_func(rcrsVar, varList, inputList):

    #-----------以下に操作に必要な変数を書く--------------
    
    #--------------------ここまで-----------------------

    answerList = list(combinations_with_replacement(inputList, 2)) #<-二つ目の変数が組合せの数を作る
    
    return answerList
#--------------------------------------------------------------------


varList1 = make_intList_func()
inputList1 = make_strList_func()

p = math.perm(len(inputList1))

print(p)