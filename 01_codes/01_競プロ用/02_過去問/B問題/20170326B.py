from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------

varList1 = make_intList_func()

studentList1 = [make_intList_func() for _ in range(varList1[0])]
checkPointList1 = [make_intList_func() for _ in range(varList1[1])]

compareTmp = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000
answer = 1

for i in range(len(studentList1)):
    for j in range(len(checkPointList1)):
        
        manhattanLength = abs(studentList1[i][0]-checkPointList1[j][0]) + abs(studentList1[i][1]-checkPointList1[j][1])
        
        print("manhattanLength: " +str(manhattanLength))
        
        if manhattanLength < compareTmp:

            print("answerTmp: " + str(compareTmp))

            answer = j+1
            compareTmp = manhattanLength
            
    print(answer)
    answer = 1
    compareTmp = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000
