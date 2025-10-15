from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------

inputList1 = make_intList_func()

Wb = inputList1[0]
Hb = inputList1[1]
N1 = inputList1[2]

areaOfBig = Wb*Hb

for i in range(N1+1):
    if i == 0:
        continue
    else:
        inputList1 = make_intList_func()
        Ws = inputList1[0]
        Hs = inputList1[1]
        Nr = inputList1[2]
        if Nr == 1:
            areaOfBig = areaOfBig - (Ws*Hb)
        elif Nr == 2:
            areaOfBig = areaOfBig - ((Wb-Ws)*Hb)
        elif Nr == 3:
            areaOfBig = areaOfBig - (Wb*Hs)
        elif Nr == 4:
            areaOfBig = areaOfBig - (Wb*(Hb-Hs))

print(areaOfBig)

#---------------------------詳細な解説-----------------------------------------
#初期化:
##各指示の処理:
#各点と対応する指示を順に処理します。
#a == 1 では x<x の領域を黒く塗るため、left を最大で Xi に更新します。
#a == 2 では x>x の領域を黒く塗るため、right を最小で Xi に更新します。
#a == 3 では y<y の領域を黒く塗るため、bottom を最大で Yi に更新します。
#a == 4 では y>y の領域を黒く塗るため、top を最小で Yi に更新します。
#白い領域の計算:
#黒く塗られた領域の境界が互いに交差する場合（left >= right または bottom >= top）、全体が黒く塗られてしまうため、白い領域の面積は0となります。
#そうでない場合、白い領域の面積は (right−left)×(top−bottom) で計算されます。
#これにより、問題の条件を満たす白い領域の面積を効率的に求めることができます。