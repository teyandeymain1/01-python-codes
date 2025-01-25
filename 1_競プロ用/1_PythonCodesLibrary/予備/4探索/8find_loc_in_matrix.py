import sys
#----------配列の内包表記による行列の作成-------------------
def make_matrix_without_numpy(y):
    #y:縦(列)  
    readline = sys.stdin.readline
    return list(list(map(int, readline().replace('\n','').replace('\r',''))) for _ in [None]*y)
                                                                        #空欄があるときは .split() をつける
                        #↑この部分を str に変えることで要素が str のリストへ
#-------------------------座標と要素を見つけて辞書にまとめる----------------------
def find_loc_in_matrix(inMatrix):
    #二次元配列から座標と要素を取り出して辞書に保存する。(今回は0になっている部分を探す)
    return {(y, x): item\
                for y, rowList in enumerate(inMatrix, start=0)\
                    for x, item in enumerate(rowList, start=0) if item == 0}
#=====================================================
readline = sys.stdin.readline
y, = map(int, readline().replace('\n','').replace('\r','').split())
#引数が一つの時はここに , を入れること                       #空欄がないときは .split() を消す

aMatrix = make_matrix_without_numpy(y)

locDict = find_loc_in_matrix(aMatrix)

print(locDict)

"""
9
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