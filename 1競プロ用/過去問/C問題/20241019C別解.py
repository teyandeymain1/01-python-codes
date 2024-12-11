import sys

def main():
    #変数定義
    readline = sys.stdin.readline
    N, = map(int, readline().replace('\n','').replace('\r','').split())
                                                                #空欄がないときは .split() を消す

    toyTuple = tuple(map(int, readline().replace('\n','').replace('\r','').split()))
                                                                            #空欄がないときは .split() を消す
    boxTuple = tuple(map(int, readline().replace('\n','').replace('\r','').split()))
                                                                            #空欄がないときは .split() を消す
    toyList = sorted(toyTuple, reverse=True)
    boxList = sorted(boxTuple, reverse=True)

    ans = 0
    boxIndex = 0
    
    for i in range(N):
        if i == N-1 and ans == 0: #最小のおもちゃの箱が無いとき
            print(toyList[N-1])
            exit()
        else:
            if toyList[i] <= boxList[boxIndex]: #箱が大きいときは、次の箱を見る
                boxIndex += 1
            else:
                if ans == 0:
                    ans = toyList[i]
                else:
                    print(-1)
                    exit()
    print(ans)
if __name__ == "__main__": 
    main()