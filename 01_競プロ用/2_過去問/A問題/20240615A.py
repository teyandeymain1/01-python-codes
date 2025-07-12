from sys import stdin
#-----------------文字のリスト-----------------------
def make_strList_func():
    readline = stdin.readline
    strList = list(map(str, readline()[:-1].split()))
    return strList
#------------------------------------------------

inputList3 = make_strList_func()

answer = "No"
if inputList3[0] == "AtCoder" and inputList3[1] == "Land":
    answer = "Yes"


print(answer)