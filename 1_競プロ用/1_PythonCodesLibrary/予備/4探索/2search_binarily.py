import sys
#-------------------二分探索-----------------------
def search_binarily(target, inTuple):
    #変数定義
    inTuple = sorted(inTuple, reverse=False) #昇順、tupleをsortedするとlistが返る
    left, right = 0, (len(inTuple) - 1) #探索する範囲の左端と右端を設定
    #
    while left <= right:                 
        mid = (left + right)//2 #探索する範囲の中央を計算   
        if inTuple[mid] == target:
            return inTuple[mid] #ぴったりの答えが見つかったら、それをそのままを返す。
        elif inTuple[mid] < target:
            left = (mid + 1)    #中央値より大きい場合は探索範囲の左を変える
        else:
            right = (mid - 1)   #中央値より小さい場合は探索範囲の右を変える
        
        #print("mid", mid, "left:", left, "right:", right)
    
    return inTuple[mid] #ぴったりの答えが無いとき、中央値から一つ右(一つ大きい)の配列内indexを返す
#----------------------(問題によって変える。今回はAtCoder 典型アルゴリズム問題集 A - 二分探索の練習問題用)------------------
def solve_problem(argTuple, inTuple):
    #変数定義
    K, index = argTuple
    #本体
    if inTuple[-1] < K:
        return -1
    else:
        return index
#======================================main==============================================-
def main():
    #変数定義
    readline = sys.stdin.readline
    N, K = map(int, readline().replace('\n','').replace('\r','').split())
                                                                #空欄がないときは .split() を消す

    aTuple = tuple(map(int, readline().replace('\n','').replace('\r','').split()))
                                                                            #空欄がないときは .split() を消す
    
    index = search_binarily(K, aTuple)
    argTuple = (K, index)
    print(solve_problem(argTuple, aTuple))

if __name__ == "__main__": 
    main()