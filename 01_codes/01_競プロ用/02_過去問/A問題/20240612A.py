from sys import stdin
#-----------------文字のリスト-----------------------
def make_strList_func():
    readline = stdin.readline
    strList = list(map(str, readline()[:-1]))
    return strList
#------------------------------------------------
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------
valList1 = make_intList_func()

row = valList1[0]

for i in range(row):
    strLine1 = make_strList_func()
    convertion1 = strLine1[0]
    convertion2 = strLine1[4]
    strLine1[0] = convertion2
    strLine1[4] = convertion1
    "".join(strLine1)
    print(*strLine1, sep = "")
    