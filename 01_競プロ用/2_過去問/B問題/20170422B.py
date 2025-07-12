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
inputList2 = make_intList_func()

if inputList1[0] > inputList2[0]:
    print("GREATER")
elif inputList1[0] < inputList2[0]:
    print("LESS")
elif inputList1[0] == inputList2[0]:
    print("EQUAL") 