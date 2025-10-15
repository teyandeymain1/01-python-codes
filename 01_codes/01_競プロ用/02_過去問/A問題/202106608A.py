from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------

inputList1 = make_intList_func()
inputList2 = make_intList_func()

n=inputList1[0]
m=inputList1[1]

i=0
while True:
    if i > n-1:
        break
    m=m-inputList2[i]
    if m<0:
        break
    else:
        i+=1
print(i)