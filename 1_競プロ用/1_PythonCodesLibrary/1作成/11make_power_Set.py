import sys
from itertools import combinations
#-------------------べき集合の作成-----------------------
def mk_pw_Set(inTuple):
    return tuple(combo for num in range(len(inTuple)+1)\
                        for combo in combinations(inTuple, num))
            #↑この部分を list や set に変える
#======================================main==============================================-
def main():
    #変数定義
    readline = sys.stdin.readline
    xs = tuple(map(int, readline().replace('\n','').replace('\r','').split()))
                                                                            #空欄がないときは .split() を消す
    print(mk_pw_Set(xs))

if __name__ == "__main__": 
    main()