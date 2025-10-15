#------------------整数のリスト-----------------------
def make_intList_func():
    intList = list(map(int, input().split()))
    return intList
#------------------------------------------------
#-----------------文字のリスト-----------------------
def make_strList_func():
    strList = list(map(str, input().split()))
    return strList
#------------------------------------------------

listInput1 = make_intList_func()
n = listInput1[0]
m = listInput1[1]
k = listInput1[2]

answer = 0

for i in range(m):
    listDist =  make_strList_func()
    for j in range(len(listDist)):
        if listDist[0] == "o":
            if 

        elif listDist[0] == "x":
   
print(listDist)

#https://atcoder.jp/contests/abc356/submissions/54090772→C - Keysの最速の回答