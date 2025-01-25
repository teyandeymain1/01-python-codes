import sys          
readline = sys.stdin.readline
aTuple = tuple(map(int, readline().replace('\n','').replace('\r','')))
                                                                    #空欄があるときは .split() をつける
            #↑この部分を list か set に変えることで list か set を作ることができる。

aList = sorted(aTuple, reverse=False) #昇順、tupleをsortedするとlistが返る

bList = sorted(aTuple, reverse=True) #降順、tupleをsortedするとlistが返る

print(aList)
print(bList)