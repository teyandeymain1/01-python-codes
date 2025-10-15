from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------
#--------------線形探索---------------------------
def search_linear_func(list):

    answer = 100000000000000000000000000000000000000000000000000000000000000000000000 #--答えの初期値を左に書く--

    for i in range(len(list)):
        answerTmp = 0      #答えの候補を保存するための変数
        swich = 0          #探索を止めるための変数
        while swich == 0:  #swich = 0の間は探索を続行

            #------------------探索を続ける条件を下に書く-----------------
            if (list[i] % 2) == 0:
                list[i] = list[i] // 2
                answerTmp += 1
            #----------------------ここまで-----------------------------
                       
            else:
                swich = 1 #swich = 1 として探索を止める
        
        if answerTmp < answer: #--答えの候補を保存する条件を左に書く--

            answer = answerTmp
    return answer #答えを返す
#------------------------------------------------

inputList1 = make_intList_func()

print(search_linear_func(inputList1))