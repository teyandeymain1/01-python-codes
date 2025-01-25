from sys import stdin
#-----------------文字のリスト-----------------------
def make_strList_func():
    readline = stdin.readline
    strList = list(map(str, readline()[:-1]))
    return strList
#------------------------------------------------

inputList1 = make_strList_func()

answer = "No"

for i in range(len(inputList1)):
    if inputList1[i] == "R":
        compareRice = i
    if inputList1[i] == "M":
        compareMiso = i
if compareRice < compareMiso:
    answer = "Yes"

print(answer)