import sys
#-------------------二分探索-----------------------
def search_binarily(target, inTuple):
    #変数定義
    inTuple = sorted(inTuple, reverse=False) #昇順、tupleをsortedするとlistが返る
    left, right = 0, (len(inTuple) - 1) #探索する範囲の左端と右端を設定
    #
    while left <= right:                 
        mid = (left + right)//2 #探索する範囲の中央を計算
        if solver("_", inTuple[mid], target) == "small":
            right = (mid - 1)   #中央値より小さい場合は探索範囲の右を変える   
        elif solver("_", inTuple[mid], target) == "big":
            left = (mid + 1)    #中央値より大きい場合は探索範囲の左を変える
        else: #solver("_", inTuple[mid], target) == "sucess"
            return mid          #ぴったりの答えが見つかったら、それをそのままを返す

        #print("mid", mid, "left:", left, "right:", right)
    
    return left #ぴったりの答えが無いとき、中央値から一つ右(一つ大きい)の配列内indexを返す
#----------------------(問題によって変える。今回はフツーの二分探索)------------------
def solver(flag, arg, target):
    #本体
    if target < arg:
        flag = "small"  #中央値より小さい場合は探索範囲の左を変える
    elif arg < target:
        flag = "big"    #中央値より大きい場合は探索範囲の右を変える
    else:
        flag = "sucess" #ぴったりの答えが見つかったら、それをそのままを返す。
    #以下変更禁止
    return flag
#======================================main==============================================-


def main():
    #変数定義
    readline = sys.stdin.readline
    N, K = map(int, readline().replace('\n','').replace('\r','').split())
                                                                #空欄がないときは .split() を消す

    aTuple = tuple(map(int, readline().replace('\n','').replace('\r','').split()))
                                                                            #空欄がないときは .split() を消す
    
    ans = search_binarily(K, aTuple)

    #AtCoder 典型アルゴリズム問題集 A - 二分探索の練習問題用のコード
    if aTuple[-1] < K:
        print(-1)
    else:
        print(ans)

if __name__ == "__main__": 
    main()