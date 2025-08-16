from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------

inputList1 = make_intList_func()

answer = inputList1[1] * ((inputList1[1]-1)**(inputList1[0]-1))

print(answer)