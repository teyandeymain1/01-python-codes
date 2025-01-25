import sys
from itertools import *
#------------------整数のリスト-----------------------
def make_intList():
    readline = sys.stdin.readline
    intList = list(map(int, readline()[:-1].split()))
    return intList
#------------------------------------------------
#-----------------配列内の要素の累積和-------------------------
def cum_sum_items_in_list(rcrsVar, varList, inputList):

    #-----------以下に操作に必要な変数を書く--------------
    varList = []
    #--------------------ここまで-----------------------

    varList = list(accumulate(inputList))
    
    return varList
#--------------------------------------------------------------------
#-----------------配列内の要素の累積積-------------------------
def cum_prod_items_in_list(rcrsVar, varList, inputList):
    import operator

    #-----------以下に操作に必要な変数を書く--------------
    varList = []
    #--------------------ここまで-----------------------

    varList = list(accumulate(inputList, operator.mul))
    
    return varList
#--------------------------------------------------------------------
#-----------------配列内の要素の累積最小値-------------------------
def cum_min_items_in_list(rcrsVar, varList, inputList):

    #-----------以下に操作に必要な変数を書く--------------
    varList = []
    #--------------------ここまで-----------------------

    varList = list(accumulate(inputList, min))
    
    return varList
#-------------------------------------------------------------------
#-----------------配列内の要素の累積最大値-------------------------
def cum_max_items_in_list(rcrsVar, varList, inputList):

    #-----------以下に操作に必要な変数を書く--------------
    varList = []
    #--------------------ここまで-----------------------

    varList = list(accumulate(inputList, max))
    
    return varList
#--------------------------------------------------------------------
#-----------------配列内の要素の累積和( initial = 0 で配列の初めに初期値 0 が追加される)-------------------------
def cum_sum_items_plusIni_in_list(rcrsVar, varList, inputList):

    #-----------以下に操作に必要な変数を書く--------------
    varList = []
    #--------------------ここまで-----------------------

    varList = list(accumulate(inputList, initial = 0))
    
    return varList
#--------------------------------------------------------------------

varList1 = make_intList()
inputList1 = make_intList()

#---------関数内に追加したい変数を配列の最後に追加------------- 
#----------------------ここまで-----------------------------

answerList1 = cum_sum_items_in_list(0, varList1, inputList1)
answerList2 = cum_prod_items_in_list(0, varList1, inputList1)
answerList3 = cum_min_items_in_list(0, varList1, inputList1)
answerList4 = cum_max_items_in_list(0, varList1, inputList1)
answerList5 = cum_sum_items_plusIni_in_list(0, varList1, inputList1)

print(answerList1)
print(answerList2)
print(answerList3)
print(answerList4)
print(answerList5)