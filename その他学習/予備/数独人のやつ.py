import time
import sys
sys.setrecursionlimit(10**6) #再帰回数の変更
from sys import stdin
#--------------------------------------整数のリスト----------------------------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline()[:-1]))
    return intList
#-------------------------配列の内包表記による行列の作成-------------------------------------
def make_matrix_without_numpy_ver_func(rcrsVar, varList, inputList):

    matrix = [make_intList_func() for _ in [None]*varList[0]]

    return matrix
#-------------------m行n列のセルに格納することが可能な数字を列挙する関数------------------------
def check_cell(t, m, n):
    n_set1, n_set2, n_set3 = set(), set(), set()
    # 行に対してのチェック
    for cell in t[m]:
        if cell != 0:
            n_set1.add(cell)
    # 列に対してのチェック
    for r in t:
        if r[n] != 0:
            n_set2.add(r[n])
    # エリアに対してのチェック
    for a in range(3 * (m // 3), 3 * (m // 3) + 3):
        for b in range(3 * (n // 3), 3 * (n // 3) + 3):
            if t[a][b] != 0:
                n_set3.add(t[a][b])
    # これら3つのsetの和集合を取る
    n_union = n_set1.union(n_set2, n_set3)
    # 差集合をとり、まだ使われていない数字を取得
    n_not_used = {1, 2, 3, 4, 5, 6, 7, 8, 9}.difference(n_union)
    # m, nに入りうる数字の集合を返す
    return n_not_used

# 空欄を入りうる数字が少ない順にソートし、その空欄の座標と候補の集合を返す関数
def sort_blank_cell(t):
    if not find_all_blank(t):
        return -1, -1
    # 空欄に入る数字の候補リストと、空欄の座標リスト
    n_list = []
    blank_cell_list = []
    # 2つのリストに値を追加
    for blank_cell in find_all_blank(t):
        blank_cell_list.append((blank_cell[0], blank_cell[1]))
        n_list.append(check_cell(t, blank_cell[0], blank_cell[1]))
    # 数字の候補リストを、集合の要素数昇順にソートするための要素番号リストを作成
    indices = [*range(len(n_list))]
    # 要素番号リストを、n_list要素数昇順にソート
    sorted_indices = sorted(indices, key=lambda i: len(n_list[i]))
    # ソートされた要素番号をもとに、n_list, blank_cell_listもソート
    n_list_sorted = [n_list[i] for i in sorted_indices]
    blank_cell_list_sorted = [blank_cell_list[i] for i in sorted_indices]

    return blank_cell_list_sorted, n_list_sorted

# 空欄をすべて取得し、2次元配列で返す関数
def find_all_blank(t):
    blank_list = []
    for i, items in enumerate(t):
        for j, item in enumerate(items):
            if item == 0:
                blank_list.append((i, j))
    return blank_list

# 数独を解く関数、候補が少ないマス目から候補を一つずつ格納
def do_v2(t):
    blank_cell_list, n_list = sort_blank_cell(t)
    # blank_cell_listに-1が格納されていれば、数独完成済み
    if blank_cell_list == -1:
        return True
    r = blank_cell_list[0][0]
    c = blank_cell_list[0][1]
    # numを格納
    for num in n_list[0]:
        t[r][c] = num
        # do_v2()関数自身を呼び出し
        if do_v2(t):
            return True
        t[r][c] = 0
    # 一つも条件を満たさなければ戻るためFalseを返す
    return False

# 完成したTABLEが実際に正しいかどうかを判定する関数
def check_table(t):
    status = True
    for r in range(9):
        for c in range(9):
            # この関数は第4引数の数値が使われていない数字かどうかを判定するため
            # 一度でもTrue -> 完成済みTABLEのどこかに重複が発生している
            if t[r][c] in check_cell(t, r, c):
                status = False
    return status

# 数独テーブルを表示する関数
def display_table(t):
    for _ in t:
        print(_)

#----------------------------------------main-------------------------------------
def main():
    rcrsVar1 = 1

    print("数独の縦と横のサイズを、縦 横の順で入力してください。(数字の間にはスペースを一つ入れてください。また、各数字は3の倍数にしてください。)")
    readline = stdin.readline
    varList1 = list(map(int, readline().split())) #数独の縦横のサイズを入力する。

    print("数独を入力してください。ただし、空欄は0で埋めてください。")
    inputList1 = []

    matrix1 = make_matrix_without_numpy_ver_func(rcrsVar1, varList1, inputList1)

    #-------時間測定開始--------
    start = time.time()
    do_v2(matrix1)
    # 完成後の数独の表示
    display_table(matrix1)
    # check_table()関数で完成後の数独が適切な状態かチェック
    w = "この解答は正しいです。" if check_table(matrix1) else "この解答は正しくありません"
    print(w)
    #-------時間測定終了--------
    end = time.time()
    print("実行時間:", (end - start))

if __name__ == "__main__": 
    main()