#----------------------------------------------
def make_intList_func():
    intList = list(map(int, input().split()))
    return intList
#------------------------------------------------

list1 = make_intList_func()  #変数リストを作成
list2 = make_intList_func() #ビンゴで読み上げられた数字リスト

N = int(list1[0])
T = int(list1[1])

row = [0] * N
col = [0] * N 
diag = [0] * 2

print(row)
print(col)
print(diag)


for i in range(T):
    print("times: " + str(i + 1))
    x = (list2[i] - 1)// N 
    y = (list2[i] - 1) % N 

    print("list2[i] - 1: " + str(list2[i] - 1))
    print("x: " + str(x))
    print("y " + str(y))

    # 横
    row[x] += 1
    print("row: " + str(row)) #各行の埋まったマスの個数
    if row[x] == N:
        print(i + 1)
        exit()
    # 縦
    col[y] += 1
    print("col: " + str(col)) #各列の埋まったマスの個数
    if col[y] == N:
        print(i + 1)
        exit()
    # 左上 - 右下 方向の斜め
    if x == y: #斜めの埋まったマスの個数
        diag[0] += 1
        if diag[0] == N:
            print(i + 1)
            exit()
    print("diag: " + str(diag))
    # 右上 - 左下 方向の斜め
    if x + y == N - 1: #斜めの埋まったマスの個数
        diag[1] += 1
        if diag[1] == N:
            print(i + 1)
            exit()
    print("diag: " + str(diag))
print(-1)