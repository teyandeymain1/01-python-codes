import sys
from heapq import *
#----------配列の内包表記による行列の作成-------------------
def make_matrix_without_numpy(y):
    #y:縦(列)  
    readline = sys.stdin.readline
    return list(list(map(int, readline().replace('\n','').replace('\r',''))) for _ in [None]*y)
                                                                        #空欄があるときは .split() をつける
                        #↑この部分を str に変えることで要素が str のリストへ
#---------------------------------------------------------------------------
class create_node: #各頂点を表現する構造体
    def __init__(self, value = 0) -> None: #インスタンスの生成&初期化
        self.left = None   #左の子頂点
        self.right = None  #右の子頂点
        self.value = value #ノードがもつ数値

class make_binary_search_tree():
    def __init__(self, inList): #インスタンスの生成&初期化
        self.root = None                    #ルートノード初期化
        for item in inList:                 #数値を持つ配列から二分木を生成
            self.insert_into_tree((item, 0)) #        
    #挿入
    def insert_into_tree(self, inList):
        #変数定義
        value = inList[0]
        node = self.root
        #
        if node == None:                 #ルートノードがNoneのとき→入力用リストの先頭の値はルートノードとして扱う
            self.root = create_node(value) #ルートノード   
            return
        else:
            #while True: #Noneでない限りparentを調べる
            for _ in range(3):

                print("value", value)
                print("前", "node.value:", node.value, "node.left:", node.left, "node.right:", node.right)

                #parent = node.value

                #次に見るノードを変える
                if value < node.value:
                    if node.left == None:  
                        node.left = create_node(value) #entryがparentのvalue以下ならば、左に進む
                        return
                elif value > node.value:
                    if node.right == None:
                        node.right = create_node(value)
                        return
                else:
                    node.value = value #entryがparentのvalueより大きいならば、右に進む
                    return
                
                print("後", "node.value:", node.value, "node.left.value:", node.left.value, "node.right.value:", node.right.value)

    # ノード node を始点に、行きがけ順でreturnListに記録する関数
    def save_node(self, argTuple, inList):
        #変数定義
        node = argTuple[0]
        returnList = argTuple[1]
        returnList.append(node.value)

        print(node)
        print(node.left)
        print(node.right)

        # ノードの左側に進み再帰する
        if node.left:
            save_node(node.left)
        # ノードの右側に進み再帰する
        if node.right:
            save_node(node.right)
        return returnList
#======================================main==============================================-
def main():
    readline = sys.stdin.readline
    y, = map(int, readline().replace('\n','').replace('\r','').split())
                                                                        #空欄がないときは .split() を消す
    aList = make_matrix_without_numpy(y)

    print(aList)
    #
    #-------------変数定義(問題によって変える。今回はAtCoder Typical Contest 002 A - 幅優先探索 用)------------
    #-----------------------ここまで----------------------------    
    #関数の実行
    make_binary_search_tree(aList)
    #print("answer", *answer)

if __name__ == "__main__": 
    main()