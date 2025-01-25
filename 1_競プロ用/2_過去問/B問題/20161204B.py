from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------

inputList1 = make_intList_func()

a=inputList1[0]
b=inputList1[1]
x=inputList1[2]

if a%x==0:
    answer = b//x-(a-1)//x
else:
    answer = b//x-a//x

print(answer)