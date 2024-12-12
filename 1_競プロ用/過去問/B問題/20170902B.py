from sys import stdin
#-----------------文字のリスト-----------------------
def make_strList_func():
    readline = stdin.readline
    strList = list(map(str, readline()[:-1]))
    return strList
#------------------------------------------------

inputList1 = make_strList_func()

print(*inputList1[0::2], sep="") #i個おきにリストの要素を表示、ただの文字列でも同じ操作ができる。