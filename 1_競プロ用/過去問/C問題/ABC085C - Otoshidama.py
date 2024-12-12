#-------------全探索-------------------
def exhaustive_seach(val2, val1):

    answer = 0
    i = 0
    j = 0
    k = 0

    #------以下書き換え-----
    if val1 < 1000:
        print("-1 -1 -1")
    #-------------------

    else:
        answer1 = -1
        answer2 = -1
        answer3 = -1
        for i in range(val2 + 1):
            for j in range(val2 - i + 1):
                k = val2 - i - j 
                #-----------------以下書き換え------------------
                if (10000 * i + 5000 * j + 1000 * k) == val1:
                    answer1 = i
                    answer2 = j
                    answer3 = k

    print(str(answer1) + " " + str(answer2) + " " + str(answer3))
#--------------------------------------------

#----------------------------------------------
def input_func_int():
    intList = list(map(int, input().split()))
    return intList
#------------------------------------------------

list1 = input_func_int()

num1 = list1[0] #枚数
num2 = list1[1] #金額

exhaustive_seach(num1, num2)