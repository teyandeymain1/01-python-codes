#----------------------------------------------
def input_func_int():
    intList = list(map(int, input().split()))
    return intList
#------------------------------------------------

num1 = int(input())

list1 = input_func_int()

m = 100000000000000000000000000000

for i in range(num1 -1):
    j = 0
    x = 0
    while (list1[i]%2) == 0:
        list1[i] = list1[i] // 2
        x += 1
    if x < m:
        m = x

print(m)