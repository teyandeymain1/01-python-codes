import sys

is 

def brackets_maker(N):
    

#---------------------------------- 行列を表示する---------------------------------------
def print_matrix(inMatrix):
    for rowList in inMatrix:         
        print("".join(map(str, rowList)))
#=====================================================
#------------------整数の行-----------------------
readline = sys.stdin.readline
N, = map(int, readline().replace('\n','').replace('\r','').split())
    #引数が一つの時はここに , を入れること                          #空欄がないときは .split() を消す


if N%2!=0:
    print()
else:
    print(brackets_maker(N))
