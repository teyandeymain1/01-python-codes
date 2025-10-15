import sys
#------------------整数の行-----------------------
readline = sys.stdin.readline
n, = map(int, readline().replace('\n','').replace('\r','').split())
    #引数が一つの時はここに , を入れること                          #空欄がないときは .split() を消す
#↑ここの , がないと一文字として認識されない。

print(n)


"""
Nが10^6 → O(N)かO(N*log(N))
Nが10^5 → O(N*log(N))かO(N*log2(N))
Nが3000 → O(N^2)
Nが300 → O(N^3)(シンプルな処理)
Nが100 → O(N^3)
Nが50 → O(N^4)
Nが20 → O(2^N)かO(N*(2^N))
"""
