import sys
#----------(str)内包表記による行列作成(str)-------------------
def mk_mtrx(y):
    #y:縦(列)  
    readline = sys.stdin.readline
    return list(list(map(str, readline().replace('\n','').replace('\r',''))) for _ in [None]*y)
                                                                        #空欄があるときは .split() をつける
#=====================================================


import sys
#----------(int)内包表記による行列作成(int)-------------------
def mk_mtrx(y):
    #y:縦(列)  
    readline = sys.stdin.readline
    return list(list(map(int, readline().replace('\n','').replace('\r','').split())) for _ in [None]*y)
                                                                        #空欄があるときは .split() をつける
#=====================================================

readline = sys.stdin.readline
y1, = map(int, readline().replace('\n','').replace('\r','').split())
#引数が一つの時はここに , を入れること                      #空欄がないときは .split() を消す

xs = mk_mtrx(y1)

print(xs)

xs[0][0] = "?"
xs[1][1] = "?"

print(xs)
