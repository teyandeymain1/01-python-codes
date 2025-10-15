import sys
#------------------文字のタプル-----------------------
readline = sys.stdin.readline
inTuple1 = tuple(map(str, readline().replace('\n','').replace('\r','')))
                                                                    #空欄があるときは .split() をつける
            #↑この部分を list か set に変えることで list か set を作ることができる。
inTuple2 = tuple(map(str, readline().replace('\n','').replace('\r','')))
                                                                    #空欄があるときは .split() をつける
            #↑この部分を list か set に変えることで list か set を作ることができる。

if inTuple1 == inTuple2:
    print(0)
elif len(inTuple1) > len(inTuple2) and inTuple1[:len(inTuple2)] == inTuple2[:len(inTuple2)]:
    print(len(inTuple2)+1)
elif len(inTuple1) < len(inTuple2) and inTuple1[:len(inTuple1)] == inTuple2[:len(inTuple1)]:
    print(len(inTuple1)+1)
else:
    for i in range(min(len(inTuple1),len(inTuple2))):
        if inTuple1[i] != inTuple2[i]:
            print(i+1)
            break