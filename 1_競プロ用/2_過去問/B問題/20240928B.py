import sys
#------------------文字のタプル-----------------------
readline = sys.stdin.readline
inTuple1 = tuple(map(str, readline()[:-1]))
            #↑この部分を list か set に変えることで list か set を作ることができる。
            #空欄があるときは .split() を使う

strList = sorted(inTuple1)

count = 0
nowLoc = 0
for item1 in strList:
    for i, item2 in enumerate(inTuple1):
        if item1 == item2 and item2 == "A":
            nowLoc = i
            break
        if item1 == item2 and i >= nowLoc:
            count += (i - nowLoc)
            break
        elif item1 == item2 and i < nowLoc:
            count += (nowLoc - i)
            break
    nowLoc = i
print(count)
