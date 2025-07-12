from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------
inputList1 = make_intList_func()

K = inputList1[0]
S = inputList1[1]

count = 0

for i in range(K+1):
    for j in range(K+1):
        for k in range(K+1):
            if (i+j+k) == S:
                count += 1
print(count)