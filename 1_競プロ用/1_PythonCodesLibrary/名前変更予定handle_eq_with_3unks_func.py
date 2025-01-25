import sys
#------------------整数のリスト-----------------------
def make_intList():
    readline = sys.stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------
#---------------------#(X+Y+Z=Const)タイプの式を1つのforループで処理するための関数---------------------------
def handle_eq_with_3unks(rcrsVal, varList, inputList):
    
    Const = inputList[1]    #Constを代入

    #-------------------以下に変数 X,Y,Z の変域(Range)を書く-------------------
    varRng1 = inputList[0] #変数 X,Y,Z の変域は 0<=X<=varRng1, 0<=Y<=varRng1, 0<=Z<=varRng1 である。
    maxYplusZ = 2*varRng1  #<-最大値を問題に応じて変更すること。今回は 0<=Y<=varRng1, 0<=Z<=varRng1 より 0<=Y+Z<=2varRng1    
    #------------------------ここまで--------------------------------------

    #-----------以下に操作に必要な変数を書く--------------
    varList[0] = 0
    #--------------------ここまで-----------------------

    for X in range(varRng1 + 1):                   # (Y+Z)=(Const−X) として X の値を固定すると、Y と Z の二変数を考えるだけで済む。
        if 0 <= (Const - X) <= maxYplusZ:
            minY = max(0, ((Const - X) - varRng1)) # Y=0 のとき、Z=2varRng1 (Y = 0, minYの最小値)、Y=(Const-X)-varRng1 のとき Z=varRng1 (Y=varRng1, minYの最大値かつmaxYの最小値)
            maxY = min(varRng1, (Const - X))       # Y=(Const-X) のとき Z=0 (Y=2varRng1, maxYの最大値)となる。 

    #------------------関数内で行う操作を下記に書く(このプログラムはAtCoder ABC051-B_Sum of Three Integers用)-------------------
            varList[0] += (maxY - minY + 1)    #取りうる Y の個数は maxY−minY+1 です。この式はminYからmaxYまでの数字の個数を数える式。
                                               #例えば、minY=0,maxY=3 のとき、整数の個数は0から3までの4つ (maxY−minY+1=3-0+1=4) 。
    #--------------------ここまで-----------------------

    return varList
#--------------------------------------------------------------------
varList1 = []
inputList1 = make_intList()

#---------関数内に追加したい変数を配列の最後に追加-------------
varList1 = varList1 + [0] #最小値を配列の最後に追加 
#----------------------ここまで-----------------------------

answer = handle_eq_with_3unks(0, varList1, inputList1)

print("Answer: " + str(answer[0]))

#--------------------------解説--------------------------------
# Z の値は Y の値に依存するため、 Z を考える必要はない。
#例えば、(Const-X)=3 の時、0<=Y+Z<=3 となり、これを満たす (Y,Z) は (0,3) (1,2) (2,1) (3,0) の４つで、これは Y の値の個数を数えることで求められる。