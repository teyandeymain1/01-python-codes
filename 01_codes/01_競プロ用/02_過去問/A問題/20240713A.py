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

inputList1 = make_intList_func()

inputStr = str(input())

if inputStr == "Red":
    print(min(inputList1[1], inputList1[2]))

elif inputStr == "Green":
    print(min(inputList1[0], inputList1[2]))

elif inputStr == "Blue":
    print(min(inputList1[0], inputList1[1]))