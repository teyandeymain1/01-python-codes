import sys
#---------------------素集合データ構造--------------------------
class make_union_find_set:
    def __init__(self) -> None: #インスタンスの生成&初期化
        self.parent = dict()    #root 辞書
        self.size = dict()      #サイズも辞書

    def make_set(self, arg): #集合の作成
        if isinstance(arg, int):
            self.parent = {i: i for i in range(arg)}
            self.size = {i: 0 for i in range(arg)}
        elif isinstance(arg, set):
            self.parent = {i: i for i in arg}
            self.size = {i: 0 for i in arg}

            print("初期parent", self.parent)
            print("初期size", self.size)
            
        else:
            sys.exit("整数か集合を入力してください")

    def find_root(self, rt):
        if self.parent[rt] == rt: #rtが根(root)ならrtを返す
            return rt
        else: #経路圧縮
            self.parent[rt] = self.find_root(self.parent[rt]) #rtが根でない場合は親parent[rt]を根に設定し再帰的に上位の親へと進む
            return self.parent[rt]

    def union_by_size(self, rt1, rt2): 
        rtS = self.find_root(rt1)
        rtB = self.find_root(rt2)

        print("前rtS", rtS, "前rtB", rtB)
        print("前parent", self.parent)
        #
        if rtS == rtB: #同じグループのときは何もしない
            return False
        #union by sizeで効率化
        if self.size[rtB] < self.size[rtS]: #rtSがrtBのほうが小さくなるようにする。
            rtB, rtS = rtS, rtB
        #rtBをrtSに併合
        self.parent[rtB] = rtS 
        self.size[rtS] += self.size[rtB]
        
        print("後rtS", rtS, "後rtB", rtB)  
        print("後parent", self.parent)
        print("size", self.size)

        return True

    def is_same(self, rt1, rt2): #rt1とrt2が同じグループに属するか判定
        return self.find_root(rt1) == self.find_root(rt2) #"=="でつながっているので返り値は"True"か"False"

    def get_size(self, x): #グループのサイズを取得
        return self.size[self.find_root(x)] 
#=====================================================
def main():
    #変数定義
    readline = sys.stdin.readline
    (N, Q) = map(int, readline().replace('\n','').replace('\r','').split())
                                                                    #空欄がないときは .split() を消す
    uf = make_union_find_set()
    uf.make_set(N) #結合するサイズを入力
    #
    for _ in range(Q):
        query, A, B = map(int, readline().replace('\n','').replace('\r','').split())
                                                                            #空欄がないときは .split() を消す
        if query == 0:
            uf.union_by_size(A, B)
        elif query == 1:  
            print("Yes" if uf.is_same(A, B) else "No")

if __name__ == "__main__": 
    main()