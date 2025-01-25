import sys
#------------------整数のリスト-----------------------
def make_intList():
    readline = sys.stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------
#---------------------#(X+Y+Z=Const)タイプの式を1つのforループで処理するための関数---------------------------
def handle_siml_linear_eq_with_3unks(rcrsVal, varList, inputList):
    
    Const = inputList[1] #Constを代入

    #-------------------以下に変数 X, Y, Z の変域(Range)を書く-------------------
    varRng1 = inputList[0]    #変数 X, Y, Z の変域は 0 <= X, Y, Z <= varRng1 である。
    #------------------------ここまで--------------------------------------

    #-----------以下に操作に必要な変数を書く--------------
    varList = [-1, -1, -1]
    Const = inputList[1]/1000 # 10000X+5000Y+1000Z=Const (Constは1000の倍数) を両辺1000で割る.
    #--------------------ここまで-----------------------

    for X in range(varRng1 + 1):               #式は 10X+5Y+Z=Const かつ X+Y+Z=varRng1 の連立方程式
        if 0 <= (Const - 9*X) <= Const:        #二つ目の式から一つ目の式を引くと 9X+4Y=Const-varRng1 になる。9X を移行して 4Y=Const-varRng1-9X
            if (Const - 9*X - varRng1)%4 == 0: # Y=(Const-varRng1-9X)/4
                Y = (Const - 9*X - varRng1)//4
                Z = varRng1 - X - Y

    #------------------関数内で行う操作を下記に書く(このプログラムはAtCoder ABC085-C_Otoshidama用)-------------------
                if Y >= 0 and Z >= 0:
                    varList[0] = int(X)
                    varList[1] = int(Y)
                    varList[2] = int(Z)
                    break
    #--------------------ここまで-----------------------

        else:
            break    

    return varList
#--------------------------------------------------------------------

varList1 = []
inputList1 = make_intList()

#---------関数内に追加したい変数を配列の最後に追加-------------
#----------------------ここまで-----------------------------

answer = handle_siml_linear_eq_with_3unks(0, varList1, inputList1)

print(*answer)