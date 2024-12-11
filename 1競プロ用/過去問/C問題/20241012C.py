import sys
#----------配列の内包表記による行列の作成-------------------
def make_matrix_without_numpy(y):
    #y:縦(列)  
    readline = sys.stdin.readline
    return list(list(map(str, readline().replace('\n','').replace('\r',''))) for _ in [None]*y)
                                                                        #空欄があるときは .split() をつける
                        #↑この部分を str に変えることで要素が str のリストへ
#---------------------------------- 行列を表示する---------------------------------------
def print_matrix(inMatrix):
    for rowList in inMatrix:         
        print("".join(map(str, rowList)))
#=====================================================
readline = sys.stdin.readline
N, = map(int, readline().replace('\n','').replace('\r','').split())
#引数が一つの時はここに , を入れること                      #空欄があるときは .split() をつける

inMatrix1 = make_matrix_without_numpy(N)
ansMatrix = [["."]*N for _ in [None]*N]

rangeTuple = tuple(range(N))
for y in rangeTuple:
    for x in rangeTuple:
        if inMatrix1[y][x] == "#":

            rot = (min(x, (N-1-x), y, (N-1-y)) + 1)%4

            if rot == 1:   #1余り=90度回転
                ansMatrix[x][(N-1)-y] = "#" 
            elif rot == 2: #2余り=180度回転
                ansMatrix[(N-1)-y][(N-1)-x] = "#"    
            elif rot == 3: #3余り=270度回転
                ansMatrix[(N-1)-x][y] = "#"                     
            else:          #0余り=0度回転
                ansMatrix[y][x] = "#"

print_matrix(ansMatrix)