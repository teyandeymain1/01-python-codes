from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------
#-----------------文字のリスト-----------------------
def make_strList_func():
    readline = stdin.readline
    strList = list(map(str, readline()[:-1].split()))
    return strList
#------------------------------------------------

valList1 = make_intList_func()

count = 0

for i in range(valList1[0]):
    inputStrRow = str(input())
    if inputStrRow == "Takahashi":
        count+=1

print(count)