import sys
from itertools import combinations
#-------------------べき集合の作成-----------------------
def make_powerSet(inTuple):
    return tuple(sum(combo) for numOfElem in range(len(inTuple)+1)\
                        for combo in combinations(inTuple, numOfElem))
            #↑この部分を list や set に変える
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
#======================================main==============================================-
def main():
    #変数定義
    readline = sys.stdin.readline
    N, = map(int, readline().replace('\n','').replace('\r','').split())
                                                                #空欄がないときは .split() を消す
    inTuple1 = tuple(map(int, readline().replace('\n','').replace('\r','').split()))
                                                                            #空欄がないときは .split() を消す
    half = sum(inTuple1)//2
    print(search_binarily(half, make_powerSet(inTuple1)))

if __name__ == "__main__": 
    main()