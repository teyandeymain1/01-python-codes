#----------------------------------------------
def input_func_int():
    intList = list(map(int, input().split()))
    return intList
#------------------------------------------------

num1 = int(input())

list1 = input_func_int()

list1 = sorted(list1, reverse=True)

sum_Alice = 0
sum_Bob = 0

for i in range(0, len(list1), 2):
    sum_Alice = sum_Alice + list1[i]

for j in range(1, len(list1), 2):
    sum_Bob = sum_Bob + list1[j]

answer = sum_Alice - sum_Bob

print(answer)