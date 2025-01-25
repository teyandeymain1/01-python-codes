import sys
#------------------整数のタプル-----------------------
readline = sys.stdin.readline
xs = tuple(map(int, readline().replace('\n','').replace('\r','').split()))
                                                                        #空欄がないときは .split() を消す
            #↑この部分を list か set に変えることで list か set を作ることができる。

print(xs)
print(*xs, sep='\n')

import sys
#------------------文字のタプル-----------------------
readline = sys.stdin.readline
xs = tuple(map(str, readline().replace('\n','').replace('\r','')))
                                                                    #空欄があるときは .split() をつける
            #↑この部分を list か set に変えることで list か set を作ることができる。

print(xs)
print(*xs, sep='\n')
