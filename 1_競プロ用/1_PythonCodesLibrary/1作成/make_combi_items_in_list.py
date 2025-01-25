import sys
from itertools import *
#------------------整数のタプル-----------------------
def make_int_tuple():
    readline = sys.stdin.readline
    return tuple(map(int, readline().replace('\n','').replace('\r','').split()))
                            #空欄がないときは .split() のかわりに [:-1] をつける
                  #↑この部分を list か set に変えることで list か set を作ることができる。
#------------------整数のリスト-----------------------
def make_list():
    readline = sys.stdin.readline
    return list(map(int, readline().replace('\n','').replace('\r','').split()))
                            #空欄がないときは .split() のかわりに [:-1] をつける
                  #↑この部分を list か set に変えることで list か set を作ることができる。
#-----------------配列内の順列(重複あり)を列挙-------------------------
def make_jjj(varList, inList):
    #変数定義
    #-----------以下に操作に必要な変数を書く--------------
    varList = []
    #--------------------ここまで-----------------------
    #
    return list(product(inList, repeat=2)) #repeat=2
#=====================================================
varList1 = make_int_tuple()
inList1 = make_list()
answerList1 = make_jjj(varList1, inList1)
print(answerList1)

#-----------------配列内の要素の組み合わせを全列挙-------------------------
def make_combi(varList, inList):
    #変数定義
    #-----------以下に操作に必要な変数を書く--------------
    varList = []
    #--------------------ここまで-----------------------
    #
    return list(combinations(inList, 2)) #<-二つ目の変数が組合せの数を作る
#=====================================================

varList1 = make_int_tuple()
inList1 = make_list()
answerList1 = make_combi(varList1, inList1)
print(answerList1)

#-----------------配列内の要素の累積積-------------------------
def make_combi_with_reps(varList, inList):
    #変数定義
    #-----------以下に操作に必要な変数を書く--------------
    varList = []
    #--------------------ここまで-----------------------
    #
    return list(combinations_with_replacement(inList, 2)) #<-二つ目の変数が組合せの数を作る
#=====================================================

varList1 = make_int_tuple()
inList1 = make_list()
answerList2 = make_combi_with_reps(varList1, inList1)

print(answerList2)