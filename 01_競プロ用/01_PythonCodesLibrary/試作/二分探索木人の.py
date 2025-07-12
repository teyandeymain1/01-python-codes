# 各頂点を表現するための構造体
class Node:
    def __init__(self, value = 0):
        self.parent = None  # 親
        self.left = None    # 左の子頂点
        self.right = None   # 右の子頂点
        self.value = value  # ノードに付随している値

# 根のノードを宣言 (insert や rec 関数のためにグローバルに置いた)
root = Node()

# 二分探索木にノード node_v を挿入する関数
def insert(node_v):
    v = node_v.value
    nex, par = root, Node()

    # 次に見るノード nex が None でない限り、
    while nex:
        # nex を調べることにする
        par = nex

        print("前", "v:", v)
        print("前", "par.parent:", par.parent, "par.value:", par.value, "par.left:", par.left, "par.right:", par.right)
        print("前", "nex.parent:", nex.parent, "nex.value:", nex.value, "nex.left:", nex.left, "nex.right:", nex.right)            

        # 値 v が今見ているノードのキー以下かそれより大きいかに応じて、
        # 次に見るノードを変える
        if v <= par.value:
            # v が par のキー以下ならば、左に進む
            nex = par.left
        else:
            # v が par のキーより大きいならば、右に進む
            nex = par.right

        print("後", "par.parent:", par.parent, "par.value:", par.value, "par.left:", par.left, "par.right:", par.right)  
        print("後", "nex:", nex)  

    # 挿入するノード node_v とその親 par について、par と node_v のつながりを作る
    if v <= par.value:
        node_v.parent = par
        par.left = node_v
    else:
        node_v.parent = par
        par.right = node_v

    print("処理終了", "par.parent:", par.parent, "par.value:", par.value, "par.left:", par.left, "par.right:", par.right)

    return


number = [] # 頂点番号を順に記録する配列

# ノード node を始点に、行きがけ順で number に記録する関数
def rec(node):
    # number に node の値を入れる (行きがけ順のため、最初に記録する)
    number.append(node.value)

    # ノードの左側に進み再帰する
    if node.left:
        rec(node.left)
    
    # ノードの右側に進み再帰する
    if node.right:
        rec(node.right)

    return


# main
Q = int(input())

for i in range(Q):
    v = int(input())

    # 最初のクエリでは root の値を設定する
    if i == 0:
        root.value = v
        continue
    
    # 値 v を入れたノード node_v を二分探索木に挿入する
    node_v = Node(v)
    insert(node_v)

# 根を始点として番号を記録する
rec(root)
# 答えを空白区切りで出力する
print(*number)