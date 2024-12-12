
import sys
#------------------整数の行-----------------------
readline = sys.stdin.readline
S = list(map(str, readline().replace('\n','').replace('\r','')))

Q, = map(int, readline().replace('\n','').replace('\r','').split())

#------------------整数のタプル-----------------------
readline = sys.stdin.readline
aTuple = tuple(map(int, readline().replace('\n','').replace('\r','').split()))
                                                                        #空欄がないときは .split() を消す
            #↑この部分を list か set に変えることで list か set を作ることができる。

def changer(var):
    if var.islower():
        return var.upper()
    else:
        return var.lower()   

bufList = []
for item in S:
    bufList.append(changer(item))

S = S + bufList

print(S)


ansList = []

for num in aTuple:
    
    print((num-1), (num-1)%(len(S)))

    if (num-1) < len(S):
        ansList.append(S[(num-1)])
    else: #num >= len(S):
        ansList.append(S[(num-1)%(len(S))])

print(*ansList)