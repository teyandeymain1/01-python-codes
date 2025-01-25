import sys
#----------配列の内包表記による行列の作成-------------------
def make_matrix(y):
    #y:縦(列)  
    readline = sys.stdin.readline
    return list(list(map(int, readline().replace('\n','').replace('\r',''))) for _ in [None]*y)
                                                                        #空欄があるときは .split() をつける
#------------------------------行列から行ごとに値を抽出------------------------------
def make_rowList(inMatrix):
    return list(map(set, inMatrix))
            #↑ここや ↑ここを set や tuple に変える
#------------------------------行列から列ごとに値を抽出-------------------------------
def make_colList(inMatrix):
    return list(set(zip(*inMatrix)))
           #↑ここや↑ここを set や tuple に変える
#----------------------行列から(3×3マス内)を抽出-------------------------
def make_SqSet(y, x, inMatrix):
    y, x = ((y//3)*3), ((x//3)*3)
    threeSqList = []
    #
    for i in range(3):
        threeSqList.extend(inMatrix[y+i][x:(x+3)]) #[row+i]は行、[col:(col+3)]は列範囲。つまり3列を3行取得してthreeSqListに加える
    return set(threeSqList)
#=====================================================
readline = sys.stdin.readline
y, x = map(int, readline().split())
                    #空欄がないときは .split() のかわりに [:-1] をつける
aMatrix  = make_matrix(y)


varSet = set(range(1, y+1))
y, x = 1, 1

existSet = make_rowList(aMatrix)[y].union(make_colList(aMatrix)[x], make_SqSet(y, x, aMatrix)) #行、列、3×3の集合を合体

ansSet = varSet - existSet #各マスに入るすべての数字の候補(9×9の数独なら1~9まで)を要素とする集合からexistSetを引く。
print("予約済み:", existSet, "答え候補:", ansSet)

""""
#補足1
0 list(map(list, inMatrix)) 
1 list(rowList for rowList in inMatrix1)
リストをつくる場合だと上記の 1 の内包表記が速い
しかし、
2 list(map(set, inMatrix)) or list(map(sum, inMatrix))
3 list(sum(rowList) for rowList in inMatrix)
関数を場合だと上記の 3 より 2 のように map() を使うほうが速い (map() は遅延評価イテレータ)

#補足2 list(list(zip(*inMatrix))) について
 * で行列を行ごとに分解 → 各行の要素を一つにまとめて処理
例
[[1,2,3], [1,2,3], [1,2,3]] → * で [1,2,3], [1,2,3], [1,2,3] の三つのリストへ分解
→ zip() で上記3つのリストの各要素をまとめて処理 → [[1,1,1], [2,2,2], [3,3,3]]
"""

#test
""""
9 9
906705402
000694000
407030509
250371086
073569120
160482057
701020605
000146000
608907201
"""