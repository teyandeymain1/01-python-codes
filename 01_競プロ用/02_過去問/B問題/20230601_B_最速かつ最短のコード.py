f=lambda:map(int,input().split())    #文字を取得

N,_=f()    #変数Nと_に代入する

A=[*f()]

for _ in range(N):A=[a-x for a,x in zip(A,f())] 
#最初の目標摂取量から後に記入された配列を列ごとに引き算していく
#マイナスなら摂取量は満たしている。プラスなら満たしていない。

print(A)

print('YNeos'[any(0<a for a in A)::2]) #詳細はYNeoで検索