import sys
#-----------------文字のリスト-----------------------
def make_strList():
    readline = sys.stdin.readline
    strList = list(map(str, readline()[:-1]))
    return strList
#=====================================================
inList2 = make_strList()

if inList2 == inList2[::-1]:
    print("Yes")
else:
    print("No")