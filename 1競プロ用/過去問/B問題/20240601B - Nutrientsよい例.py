f=lambda:map(int,input().split())

N,_=f()

A=[*f()]

print(A)

for _ in range(N):A=[a-x for a,x in zip(A,f())]
print('YNeos'[any(0<a for a in A)::2])