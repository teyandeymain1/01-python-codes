from sys import stdin
#------------------整数のリスト-----------------------
def make_intList_func():
    readline = stdin.readline
    intList = list(map(int, readline().split()))
    return intList
#------------------------------------------------

inputList1 = make_intList_func()

A = inputList1[0]
B = inputList1[1]
C = inputList1[2]

answer = "NO"

for i in range(B+1):
    if (A*i)%B == C:
        answer = "YES"
        break

print(answer)

#------------------------------------------
#A の倍数はいくつ足しても A の倍数です。よって、実は選ぶ数は 1 個だけで良いです (いくつか選んで足さなくても、最終的な総和を直接選べます)。
#次に、A%B, 2A%B, 3A%B, ... という数列を考えます。なお A%B は A を B で割ったあまりを表します。
#ここで、(k + B)A%B = (kA + BA)%B = kA%B に注目すると、この数列は周期的で、最初の B 個の要素を繰り返す数列になっていることがわかります。
#よって、この問題は A から BA まで、愚直に B で割った余りを求めて調べれば良いです。