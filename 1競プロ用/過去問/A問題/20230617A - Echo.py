#-----------------文字のリスト-----------------------
def make_strList_func():
    strList = list(map(str, input()))
    return strList
#------------------------------------------------

num1 = int(input())
strList1 = make_strList_func()

stringRow = ""

for i in range(num1):
    strList1[i] = strList1[i]+strList1[i]
    stringRow = stringRow + strList1[i]
print(stringRow)