import sys
#------------------文字のタプル-----------------------
readline = sys.stdin.readline
aTuple = tuple(map(str, readline().replace('\n','').replace('\r','')))
                                                                    #空欄があるときは .split() をつける
            #↑この部分を list か set に変えることで list か set を作ることができる。

aTuple = aTuple[1:]

ansList = []
count = 0
for item in aTuple:
    if item == "-":
        count += 1
    elif item == "|":
        ansList.append(count)
        count = 0
print(*ansList)
