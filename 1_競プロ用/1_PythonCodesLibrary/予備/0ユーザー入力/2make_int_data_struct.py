import sys
#------------------整数のタプル-----------------------
readline = sys.stdin.readline
aTuple = tuple(map(int, readline().replace('\n','').replace('\r','').split()))
                                                                        #空欄がないときは .split() を消す
            #↑この部分を list か set に変えることで list か set を作ることができる。

print(aTuple)
print(*aTuple, sep='\n')

import sys
#------------------文字のタプル-----------------------
readline = sys.stdin.readline
aTuple = tuple(map(str, readline().replace('\n','').replace('\r','')))
                                                                    #空欄があるときは .split() をつける
            #↑この部分を list か set に変えることで list か set を作ることができる。

print(aTuple)
print(*aTuple, sep='\n')

"""
Nが10^6 → O(N)かO(N*log(N))
Nが10^5 → O(N*log(N))かO(N*log2(N))
Nが3000 → O(N^2)
Nが300 → O(N^3)(シンプルな処理)
Nが100 → O(N^3)
Nが50 → O(N^4)
Nが20 → O(2^N)かO(N*(2^N))
"""