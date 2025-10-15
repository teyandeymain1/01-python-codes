#------------------整数のリスト-----------------------
def make_intList_func():
    intList = list(map(int, input().split()))
    return intList
#------------------------------------------------
list1 = make_intList_func()

sumOfPower = 0

for i in range(64):
    sumOfPower = sumOfPower +  (2 ** i) * list1[i]

print(sumOfPower)