from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------

def plusfunc(x):
    return x+1

inputList1 = make_intList_func()

N = inputList1[0]
T = inputList1[1]
P = inputList1[2]

inputList2 = make_intList_func()

flag = "down"
count = 0
answer = 0

while flag == "down":    
    for j in inputList2:

        print(j)

        if j >= T:
            count += 1


    if count >= P:
        print(answer)
        exit()
    inputList2 = list(map(lambda x: x+1, inputList2))
    answer += 1
    count = 0

    print(inputList2)
