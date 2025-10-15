from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------

readline = stdin.readline
N = int(readline()[:-1])
K = int(readline()[:-1])

inputList1 = make_intList_func()

answer = 0

for i in inputList1:
    if i <= K//2:
        answer += i*2

    elif i >= K//2:
        answer += (K-i)*2
    
print(answer)