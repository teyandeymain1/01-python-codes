from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------

inputList1 = make_intList_func()

intList1 = [1,2,3]
intList2 = [4,5,6]
intList3 = [7,8,9]

answer = "No"

for i in range(2):
    if intList1[i]==inputList1[0] and intList1[i+1]==inputList1[1]:
        answer = "Yes"
    elif intList2[i]==inputList1[0] and intList2[i+1]==inputList1[1]:
        answer = "Yes"
    elif intList3[i]==inputList1[0] and intList3[i+1]==inputList1[1]:
        answer = "Yes"
print(answer)