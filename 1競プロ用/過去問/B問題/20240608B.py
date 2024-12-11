from sys import stdin#-----------------文字のリスト-----------------------
def make_strList_func():
    readline = stdin.readline
    strList = list(map(str, readline()[:-1]))
    return strList
#------------------------------------------------

inputList1 = make_strList_func()

big = 0
small = 0

for i in range(len(inputList1)):
    if inputList1[i].isupper() == True:
        big +=1
    elif inputList1[i].islower() == True:
        small +=1

strLine = ""
for j in range(len(inputList1)):
    strLine = strLine + inputList1[j]

if big>small:
    answer = strLine.upper() 
else:
    answer = strLine.lower()

print(answer)