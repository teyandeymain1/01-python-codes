from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------
#-----------------文字のリスト-----------------------
def make_strList_func():
    readline = stdin.readline
    strList = list(map(str, readline()[:-1]))
    return strList
#------------------------------------------------

varList1 = make_intList_func()

answer = "No"
startPlace = 0
count = 0

if varList1[0] == 0 or varList1[1] == 0:
    answer = "No"

elif varList1[0] > varList1[1]:
    matrix1 = [make_strList_func() for _ in range(varList1[0])]
    matrix2 = [make_strList_func() for _ in range(varList1[1])]

    for i in range(varList1[0]):
        matrix1Tmp = matrix1[i]
        flag = "down"
        for j in range(varList1[0]-varList1[1]+1):
            
            print("縦:" + str(i+1) +" 横:(" + str(j+1) +"->"+ str(j+varList1[1]) + ")")
            print(matrix1Tmp[j:j+varList1[1]])
            print(matrix2[count])

            if matrix1Tmp[j:j+varList1[1]] == matrix2[count]:
                flag = "up"
                startPlace = j
                count += 1
                if count == varList1[1]:
                    answer = "Yes"
                    print(answer)
                    exit()

            if startPlace != j:
                count = 0

            print("回数:" + str(count))
            print("開始位置:" + str(startPlace+1))
            print(flag)

        if flag == "down":       
            count = 0

print(answer)