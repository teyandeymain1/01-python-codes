
from sys import stdin

#-----------------文字のリスト-----------------------
def make_strList_func():
    readline = stdin.readline
    strList = list(map(str, readline()[:-1].split()))
    return strList
#------------------------------------------------
readline = stdin.readline
N = int(readline()[:-1])

inputList1 = []

for i in [0]*N:
    inputList1 += make_strList_func()

inputList1.append("?")

print(inputList1)

answer ="Yes"

for i in range(N-2):
    if inputList1[i] == "sweet" and inputList1[i+1] == "sweet":
        answer = "No"

print(answer)