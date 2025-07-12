import sys
from itertools import combinations
#-------------------べき集合の作成-----------------------
def make_powerSet(inTuple):
    return tuple(combo for nmOfElem in range(len(inTuple)+1)\
                        for combo in combinations(inTuple, nmOfElem))
            #↑この部分を list や set に変える
#======================================main==============================================-
def main():
    #変数定義
    readline = sys.stdin.readline
    aTuple = tuple(map(int, readline().replace('\n','').replace('\r','').split()))
                                                                            #空欄がないときは .split() を消す
    print(make_powerSet(aTuple))

if __name__ == "__main__": 
    main()