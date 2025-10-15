import sys
#------------------整数の行-----------------------
readline = sys.stdin.readline
N, = map(int, readline().replace('\n','').replace('\r','').split())
    #引数が一つの時はここに , を入れること                          #空欄がないときは .split() を消す
#↑ここの , がないと一文字として認識されない。

print(N)