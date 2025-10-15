#-------------全探索-------------------
def seach_exhaustively_func(var1, var2, var3, var4):

    answer = 0
    i = 0
    j = 0
    k = 0

    #---------以下に関数内で行う操作を書く---------
    if var1 < 100:
        answer = 1
    #--------------ここまで------------------

    else:
        for i in range(var2 + 1):
            for j in range(var3 + 1):
                for k in range(var4 + 1):

                    #---------以下に関数内で行う操作を書く---------
                    if (500 * i + 100 * j + 50 * k) == var1:
                        answer += 1
                    #--------------ここまで------------------
                    
    return answer
#---------------------------------------
from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------

inputList1 = make_intList_func()

num1 = inputList1[3] #枚数
num2 = inputList1[0] #金額
num3 = inputList1[1] #金額
num4 = inputList1[2] #金額

print(seach_exhaustively_func(num1, num2, num3, num4))