import sys
#----------配列の内包表記による行列の作成-------------------
def make_matrix_without_numpy(varTuple):
    y = varTuple[0] #縦    
    readline = sys.stdin.readline
    return list(list(map(str, readline()[:-1])) for _ in [0]*y)
                         #↑この部分を int に変えることで要素が int のリストへ
                         #intの時は[:-1]を消せ
                         #空欄があるときは .split() を使う
#=====================================================
matrix1 = make_matrix_without_numpy((12, ))

count = 0
for y, rowList in enumerate(matrix1, start = 1):
    if len(rowList) == y:
        count += 1
print(count)
