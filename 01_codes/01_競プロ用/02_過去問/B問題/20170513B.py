from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#-------------------------------------------------------
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------

varList1 = make_intList_func()

inputList = []


for i in range(varList1[1]):
    inputList += make_intList_func()

print(inputList)

countList = [0]*varList1[0]

for j in range(varList1[0]):
    for k in range(len(inputList)):
        if inputList[k] == (j+1):
            countList[j] += 1
            
    print(countList)

for l in range(varList1[0]):
    print(countList[l])